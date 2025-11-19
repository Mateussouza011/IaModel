import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go

# Configuração da Página
st.set_page_config(
    page_title="Seguro Médico - Previsão Inteligente",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DESIGN SYSTEM & CSS (DARK MODE) ---
st.markdown("""
<style>
    /* Importando fonte moderna */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #FAFAFA;
    }

    /* Fundo principal Dark */
    .stApp {
        background-color: #0E1117;
    }

    /* Sidebar Dark */
    [data-testid="stSidebar"] {
        background-color: #262730;
    }

    /* Cards Escuros com sombra suave */
    .css-1r6slb0, .css-12oz5g7, .stMarkdown { 
        /* background-color: #1E1E1E; */
    }

    /* Estilização dos Inputs (Dark) */
    .stTextInput > div > div > input, .stSelectbox > div > div > div, .stNumberInput > div > div > input {
        background-color: #262730;
        color: white;
        border: 1px solid #4A4A4A;
        border-radius: 8px;
    }
    
    /* Sliders */
    .stSlider > div > div > div > div {
        background-color: #FF4B4B;
    }

    /* Botão Principal com Gradiente (Neon Glow) */
    .stButton > button {
        background: linear-gradient(90deg, #FF4B4B 0%, #D93030 100%);
        color: white;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 10px rgba(255, 75, 75, 0.2);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 20px rgba(255, 75, 75, 0.6);
    }

    /* Títulos */
    h1, h2, h3 {
        color: #FAFAFA !important;
        font-weight: 700;
    }
    
    /* Métricas Customizadas Dark */
    .custom-metric {
        background: #262730;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #FF4B4B;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .metric-label {
        color: #A0A0A0;
        font-size: 0.9rem;
        text-transform: uppercase;
        font-weight: 600;
    }
    .metric-value {
        color: #FAFAFA;
        font-size: 2rem;
        font-weight: 700;
    }
    
    /* Ajuste de textos gerais */
    p, label, .stMarkdown {
        color: #E0E0E0;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=100)
    st.title("Painel de Controle")
    st.markdown("Configure os parâmetros abaixo para simular o perfil do segurado.")
    st.markdown("---")
    st.info("💡 **Dica:** O IMC e o Tabagismo são os fatores que mais influenciam no custo final.")

# --- HEADER ---
col_header1, col_header2 = st.columns([3, 1])
with col_header1:
    st.title("Previsão de Custos de Saúde")
    st.markdown("Utilize nossa Inteligência Artificial para obter estimativas precisas de seguro médico.")

# --- DADOS ---
API_URL = "http://127.0.0.1:8005/predict"

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
    return pd.read_csv(url)

df = load_data()

# --- TABS ---
tab_sim, tab_dash = st.tabs(["🚀 Simulador", "📊 Dashboard Analítico"])

# --- TAB 1: SIMULADOR ---
with tab_sim:
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Container para o Formulário
    with st.container():
        st.subheader("👤 Perfil do Beneficiário")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.slider("Idade", 18, 100, 30, step=1, help="Idade do beneficiário")
            sex = st.selectbox("Gênero", ["male", "female"], format_func=lambda x: "Masculino" if x == "male" else "Feminino")
        
        with col2:
            bmi = st.slider("IMC (Índice de Massa Corporal)", 10.0, 60.0, 25.0, step=0.1)
            children = st.slider("Número de Filhos", 0, 10, 0, step=1)
            
        with col3:
            smoker = st.selectbox("Fumante?", ["yes", "no"], format_func=lambda x: "Sim 🚬" if x == "yes" else "Não 🚭")
            region_map = {"southwest": "Sudoeste", "southeast": "Sudeste", "northwest": "Noroeste", "northeast": "Nordeste"}
            region = st.selectbox("Região", list(region_map.keys()), format_func=lambda x: region_map[x])

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("CALCULAR PREVISÃO AGORA", type="primary"):
        payload = {"age": age, "sex": sex, "bmi": bmi, "children": children, "smoker": smoker, "region": region}
        
        try:
            with st.spinner('Analisando perfil...'):
                response = requests.post(API_URL, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                custo = result["predicted_charges"]
                media_dataset = df['charges'].mean()
                
                st.markdown("---")
                st.subheader("🎯 Resultado da Análise")
                
                res_col1, res_col2 = st.columns([1, 1])
                
                with res_col1:
                    # Card de Resultado Dark
                    st.markdown(f"""
                    <div class="custom-metric">
                        <div class="metric-label">Custo Estimado Anual</div>
                        <div class="metric-value">US$ {custo:,.2f}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if custo > media_dataset:
                        st.warning(f"⚠️ Este valor está **US$ {custo - media_dataset:,.2f} acima** da média global.")
                    else:
                        st.success(f"✅ Este valor está **US$ {media_dataset - custo:,.2f} abaixo** da média global.")

                with res_col2:
                    # Gráfico Gauge (Velocímetro) Dark
                    fig = go.Figure(go.Indicator(
                        mode = "gauge+number+delta",
                        value = custo,
                        domain = {'x': [0, 1], 'y': [0, 1]},
                        title = {'text': "Termômetro de Custo", 'font': {'size': 24, 'color': 'white'}},
                        delta = {'reference': media_dataset, 'increasing': {'color': "#FF4B4B"}, 'decreasing': {'color': "#00CC96"}},
                        gauge = {
                            'axis': {'range': [None, 65000], 'tickwidth': 1, 'tickcolor': "white"},
                            'bar': {'color': "#FF4B4B"},
                            'bgcolor': "#262730",
                            'borderwidth': 2,
                            'bordercolor': "#4A4A4A",
                            'steps': [
                                {'range': [0, 15000], 'color': '#1E3A2F'},
                                {'range': [15000, 30000], 'color': '#3A2E1E'},
                                {'range': [30000, 65000], 'color': '#3A1E1E'}],
                            'threshold': {
                                'line': {'color': "red", 'width': 4},
                                'thickness': 0.75,
                                'value': media_dataset}}))
                    
                    fig.update_layout(
                        paper_bgcolor="#0E1117",
                        font={'color': "white"},
                        height=300, 
                        margin=dict(l=20, r=20, t=50, b=20)
                    )
                    st.plotly_chart(fig, use_container_width=True)

            else:
                st.error("Erro ao processar a solicitação.")
                
        except Exception as e:
            st.error(f"Erro de conexão: {e}")

# --- TAB 2: DASHBOARD ---
with tab_dash:
    st.subheader("🔍 Explorando os Dados Históricos")
    
    row1_col1, row1_col2 = st.columns(2)
    
    with row1_col1:
        # Gráfico Interativo 1 (Dark Template)
        fig_scatter = px.scatter(df, x="age", y="charges", color="smoker", size="bmi",
                               title="Impacto da Idade e Fumo no Custo",
                               color_discrete_map={"yes": "#FF4B4B", "no": "#00CC96"},
                               hover_data=['sex', 'region'],
                               template="plotly_dark")
        fig_scatter.update_layout(paper_bgcolor="#0E1117", plot_bgcolor="#0E1117")
        st.plotly_chart(fig_scatter, use_container_width=True)
        
    with row1_col2:
        # Gráfico Interativo 2 (Dark Template)
        fig_box = px.box(df, x="region", y="charges", color="sex",
                         title="Distribuição de Custos por Região e Gênero",
                         color_discrete_sequence=["#00CC96", "#FF4B4B"],
                         template="plotly_dark")
        fig_box.update_layout(paper_bgcolor="#0E1117", plot_bgcolor="#0E1117")
        st.plotly_chart(fig_box, use_container_width=True)
    
    st.markdown("### 📋 Dados Brutos")
    st.dataframe(df, use_container_width=True)

    st.markdown("---")
    st.subheader("🔥 Mapa de Correlação")
    st.markdown("Veja como cada variável influencia o custo (Charges). Cores mais quentes indicam maior influência.")
    
    # Preparar dados para correlação (converter categóricos para numéricos simples para visualização)
    df_corr = df.copy()
    df_corr['sex'] = df_corr['sex'].apply(lambda x: 1 if x == 'male' else 0)
    df_corr['smoker'] = df_corr['smoker'].apply(lambda x: 1 if x == 'yes' else 0)
    df_corr['region'] = df_corr['region'].astype('category').cat.codes
    
    corr = df_corr.corr()
    
    fig_corr = px.imshow(corr, text_auto=True, aspect="auto",
                         color_continuous_scale='RdBu_r',
                         title="Matriz de Correlação")
    fig_corr.update_layout(paper_bgcolor="#0E1117", plot_bgcolor="#0E1117", font={'color': "white"})
    st.plotly_chart(fig_corr, use_container_width=True)
