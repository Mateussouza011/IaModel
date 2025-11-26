import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns

st.set_page_config(
    page_title="Avaliação de Diamantes - IA",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
        color: #E0E0E0;
    }

    /* Background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(15, 12, 41, 0.95);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Inputs */
    .stTextInput > div > div > input, .stSelectbox > div > div > div, .stNumberInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.05);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
    }

    /* Sliders */
    .stSlider > div > div > div > div {
        background-color: #00d2ff;
    }

    /* Button */
    .stButton > button {
        background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%);
        color: white;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        box-shadow: 0 0 20px rgba(0, 210, 255, 0.3);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 30px rgba(0, 210, 255, 0.6);
    }

    /* Headings */
    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 700;
        text-shadow: 0 0 10px rgba(0, 210, 255, 0.5);
    }

    /* Custom Metric Card */
    .custom-metric {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        text-align: center;
    }
    .metric-label {
        color: #a0a0a0;
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 0.5rem;
    }
    .metric-value {
        color: #00d2ff;
        font-size: 3.5rem;
        font-weight: 700;
        text-shadow: 0 0 20px rgba(0, 210, 255, 0.4);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("💎 Avaliação de Diamantes")
    st.markdown("Configure as características do diamante para obter uma estimativa de preço baseada em IA.")
    st.markdown("---")
    st.info("💡 **Dica:** O **Peso (Quilates)** e a **Qualidade do Corte** são os fatores que mais influenciam no preço.")

st.title("Previsão de Preço de Diamantes")
st.markdown("Avaliação avançada com IA baseada nos 4Cs (Quilates, Corte, Cor, Pureza) e dimensões.")

API_URL = "https://web-production-94f5d.up.railway.app/predict"

@st.cache_data
def load_dataset():
    try:
        return pd.read_csv("data/diamonds.csv")
    except:
        return sns.load_dataset('diamonds')

df = load_dataset()

tab_sim, tab_dash = st.tabs(["💎 Ferramenta de Avaliação", "📊 Análise de Mercado"])

with tab_sim:
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.container():
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("Os 4 Cs (Qualidade)")
            
            # Carat
            carat = st.slider(
                "Peso (Quilates)", 
                0.2, 5.0, 1.0, step=0.01,
                help="O peso do diamante. 1 Quilate = 0.2 gramas. Quanto maior, mais raro e caro."
            )
            
            # Cut
            cut_map = {
                "Ideal": "Ideal (Perfeito)",
                "Premium": "Premium (Excelente)",
                "Very Good": "Muito Bom",
                "Good": "Bom",
                "Fair": "Aceitável (Baixo)"
            }
            cut = st.selectbox(
                "Qualidade do Corte", 
                options=["Ideal", "Premium", "Very Good", "Good", "Fair"],
                format_func=lambda x: cut_map[x],
                help="Determina o brilho do diamante. O corte 'Ideal' reflete quase toda a luz."
            )
            
            # Color
            color_map = {
                "D": "D (Incolor - Melhor)",
                "E": "E (Incolor)",
                "F": "F (Incolor)",
                "G": "G (Quase Incolor)",
                "H": "H (Quase Incolor)",
                "I": "I (Ligeiramente Amarelado)",
                "J": "J (Ligeiramente Amarelado - Pior)"
            }
            color = st.selectbox(
                "Cor", 
                options=["D", "E", "F", "G", "H", "I", "J"],
                format_func=lambda x: color_map[x],
                help="A ausência de cor é mais valiosa. D é o mais raro e puro."
            )
            
            # Clarity
            clarity_map = {
                "IF": "IF (Internamente Puro - Melhor)",
                "VVS1": "VVS1 (Inclusões Minúsculas 1)",
                "VVS2": "VVS2 (Inclusões Minúsculas 2)",
                "VS1": "VS1 (Inclusões Muito Pequenas 1)",
                "VS2": "VS2 (Inclusões Muito Pequenas 2)",
                "SI1": "SI1 (Inclusões Pequenas 1)",
                "SI2": "SI2 (Inclusões Pequenas 2)",
                "I1": "I1 (Inclusões Visíveis - Pior)"
            }
            clarity = st.selectbox(
                "Pureza (Clareza)", 
                options=["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"],
                format_func=lambda x: clarity_map[x],
                help="Mede a presença de imperfeições internas. IF é livre de imperfeições."
            )
            
        with col2:
            st.subheader("Dimensões ")
            st.markdown("Tamanho físico da pedra.")
            x = st.slider("Comprimento (x)", 0.0, 15.0, 6.0, step=0.1, help="Comprimento do diamante.")
            y = st.slider("Largura (y)", 0.0, 60.0, 6.0, step=0.1, help="Largura do diamante.")
            z = st.slider("Profundidade (z)", 0.0, 35.0, 4.0, step=0.1, help="Profundidade (altura) do diamante.")
            
        with col3:
            st.subheader("Proporções Técnicas")
            with st.expander("Ver Detalhes Avançados"):
                st.markdown("""
                Estas medidas afetam como a luz viaja dentro do diamante.
                - **Profundidade %**: Altura total dividida pela largura média.
                - **Mesa %**: Largura do topo plano dividida pela largura total.
                """)
                depth = st.slider("Profundidade % (Depth)", 40.0, 80.0, 60.0, step=0.1, help="A altura total dividida pela largura média. Afeta o brilho.")
                table = st.slider("Mesa % (Table)", 40.0, 100.0, 57.0, step=0.1, help="A largura da faceta superior plana em relação à largura total.")

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("ESTIMAR PREÇO DE MERCADO", type="primary"):
        payload = {
            "carat": carat, "cut": cut, "color": color, "clarity": clarity,
            "depth": depth, "table": table, "x": x, "y": y, "z": z
        }
        
        try:
            with st.spinner('Calculando avaliação com IA...'):
                response = requests.post(API_URL, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                price = result["predicted_price"]
                
                st.markdown("---")
                
                col_res1, col_res2 = st.columns([1, 1])
                
                with col_res1:
                    st.markdown(f"""
                    <div class="custom-metric">
                        <div class="metric-label">Valor Estimado de Mercado</div>
                        <div class="metric-value">US$ {price:,.2f}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                with col_res2:
                    fig = go.Figure(go.Indicator(
                        mode = "gauge+number",
                        value = price,
                        domain = {'x': [0, 1], 'y': [0, 1]},
                        title = {'text': "Faixa de Preço", 'font': {'size': 20, 'color': 'white'}},
                        gauge = {
                            'axis': {'range': [0, 20000], 'tickwidth': 1, 'tickcolor': "white"},
                            'bar': {'color': "#00d2ff"},
                            'bgcolor': "rgba(255,255,255,0.05)",
                            'borderwidth': 2,
                            'bordercolor': "rgba(255,255,255,0.1)",
                            'steps': [
                                {'range': [0, 5000], 'color': 'rgba(0, 210, 255, 0.1)'},
                                {'range': [5000, 10000], 'color': 'rgba(0, 210, 255, 0.2)'},
                                {'range': [10000, 20000], 'color': 'rgba(0, 210, 255, 0.3)'}
                            ]
                        }
                    ))
                    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "white"}, height=250)
                    st.plotly_chart(fig, use_container_width=True)
                    
            else:
                st.error(f"Erro: {response.text}")
                
        except Exception as e:
            st.error(f"Erro de Conexão. A API está rodando? {e}")

with tab_dash:
    st.subheader("Tendências de Mercado")
    st.markdown("Explore como as características influenciam o valor dos diamantes no mercado.")
    
    col_d1, col_d2 = st.columns(2)
    
    with col_d1:
        fig_scatter = px.scatter(df, x="carat", y="price", color="cut",
                               title="Preço vs Quilates (por Corte)",
                               labels={"carat": "Quilates", "price": "Preço (US$)", "cut": "Corte"},
                               template="plotly_dark",
                               color_discrete_sequence=px.colors.qualitative.Pastel)
        fig_scatter.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_scatter, use_container_width=True)
        
    with col_d2:
        fig_box = px.box(df, x="color", y="price", color="clarity",
                         title="Distribuição de Preço por Cor e Pureza",
                         labels={"color": "Cor", "price": "Preço (US$)", "clarity": "Pureza"},
                         template="plotly_dark")
        fig_box.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_box, use_container_width=True)
