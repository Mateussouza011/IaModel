# 💎 Previsão de Preço de Diamantes com IA

> **Projeto de Machine Learning** | Redes Neurais com TensorFlow | API REST + Interface Web

---

## 📁 Estrutura do Projeto

```
IaModel/
├── models/                     → Modelos treinados (.keras + preprocessor)
│   ├── model1.keras            → Rede Neural Simples (64→32→1)
│   ├── model2.keras            → Rede Neural com Dropout (128→64→32→1)
│   └── preprocessor.joblib     → Pré-processador de dados
├── notebooks/
│   └── treinamentoPredictDiamantes.ipynb  → Notebook de treinamento (Colab)
├── src/
│   ├── api.py                  → API REST (FastAPI)
│   └── frontend.py             → Interface Web (Streamlit)
└── scripts/                    → Scripts de execução
```

---

## 🎯 Roteiro da Apresentação

### 1. Introdução (2 min)

> 💡 *"Criamos uma IA que aprende a precificar diamantes automaticamente, analisando características físicas e retornando uma estimativa de preço em dólares."*

**Demonstração rápida:** Acesse `http://localhost:8501`

**Problema resolvido:** Avaliação manual de diamantes é subjetiva e demorada. Nossa IA padroniza e acelera esse processo.

---

### 2. Os Dados (3 min)

#### Dataset: Diamonds (Kaggle/Seaborn)

| Característica | Significado | Tipo |
|----------------|-------------|------|
| **Carat** | Peso em quilates | Numérico |
| **Cut** | Qualidade do corte | Categórico (Fair → Ideal) |
| **Color** | Cor da pedra | Categórico (D=melhor → J=pior) |
| **Clarity** | Clareza interna | Categórico (I1 → IF) |
| **Depth** | Profundidade (%) | Numérico |
| **Table** | Largura do topo (%) | Numérico |
| **X, Y, Z** | Dimensões em mm | Numérico |

#### Estatísticas do Dataset

| Métrica | Valor |
|---------|-------|
| 📊 Total de diamantes | **53.940** |
| 🎯 Divisão treino/teste | **80% / 20%** |
| 📈 Características | **9 features** |
| 💰 Preço médio | **~$3.933** |
| 💎 Preço máximo | **$18.823** |

#### Células do Notebook para mostrar:

| Célula | Conteúdo | O que explicar |
|--------|----------|----------------|
| **5** | `df.head()` - Primeiros dados | **"Vamos ver como são os dados reais"** - Mostra as primeiras 5 linhas do dataset com todas as características de cada diamante |
| **6** | `df.describe()` - Estatísticas | **"Entendendo a distribuição"** - Média, mediana, min/max de cada variável. Destaque: preços variam de $326 a $18.823! |
| **10** | Histograma e Boxplot de preços | **"A maioria dos diamantes são baratos"** - Gráfico mostra que poucos diamantes custam mais de $10.000, distribuição concentrada em valores baixos |
| **12** | Heatmap de correlação | **"Carat é TUDO!"** - Matriz colorida onde vermelho = correlação forte. Carat vs Price = 0.92 (quase perfeita). Dimensões X,Y,Z também importantes |
| **14** | Scatter Carat vs Price | **"Visualização da relação peso × preço"** - Cada ponto é um diamante. Linha clara ascendente: quanto mais pesado, mais caro. Base da nossa IA! |

> 💡 **Dica de apresentação:** Na célula 12, aponte para o quadrado vermelho escuro entre Carat e Price - essa é a "descoberta" que nossa IA vai aprender!

---

### 3. A Inteligência Artificial (5 min)

> 🧠 *"Redes neurais funcionam como um cérebro artificial: recebem dados, aprendem padrões e fazem previsões."*

#### Arquitetura dos Modelos

```
MODELO 1 (Simples)              MODELO 2 (Com Regularização)
┌─────────────────┐             ┌─────────────────┐
│   Input (9)     │             │   Input (9)     │
└────────┬────────┘             └────────┬────────┘
         │                               │
┌────────▼────────┐             ┌────────▼────────┐
│  Dense(64,ReLU) │             │ Dense(128,ReLU) │
└────────┬────────┘             └────────┬────────┘
         │                               │
┌────────▼────────┐             ┌────────▼────────┐
│  Dense(32,ReLU) │             │  Dropout(20%)   │
└────────┬────────┘             └────────┬────────┘
         │                               │
┌────────▼────────┐             ┌────────▼────────┐
│   Output (1)    │             │  Dense(64,ReLU) │
└─────────────────┘             └────────┬────────┘
                                         │
                                ┌────────▼────────┐
                                │  Dense(32,ReLU) │
                                └────────┬────────┘
                                         │
                                ┌────────▼────────┐
                                │   Output (1)    │
                                └─────────────────┘
```

#### Hiperparâmetros de Treinamento

| Parâmetro | Valor | Por quê? |
|-----------|-------|----------|
| **Épocas** | 50 | Suficiente para convergência |
| **Batch Size** | 32 | Balanço entre velocidade e precisão |
| **Validation Split** | 20% | Monitorar overfitting |
| **Optimizer** | Adam | Adaptativo, eficiente |
| **Loss** | MSE | Padrão para regressão |

#### Células do Notebook:

| Célula | Conteúdo |
|--------|----------|
| 16 | Pré-processamento (OneHotEncoder + StandardScaler) |
| 18 | Definição da arquitetura dos modelos |
| 19 | Treinamento (model.fit) |
| 21 | Gráfico de histórico de treino (loss × epochs) |

---

### 4. Resultados (3 min)

> 📊 *"MAE = Erro Médio Absoluto. Se o MAE é $500, significa que em média erramos $500 no preço."*

#### Métricas de Performance

| Modelo | MAE (Erro Médio) | Interpretação |
|--------|------------------|---------------|
| Modelo 1 | ~$280 | Erra em média $280 |
| Modelo 2 | ~$275 | Levemente melhor com Dropout |
| **Ensemble (Voting)** | **~$270** | Média dos dois é mais estável |

#### Como funciona o Voting?
```python
preço_final = (modelo1.predict() + modelo2.predict()) / 2
```

#### Células do Notebook:

| Célula | Conteúdo |
|--------|----------|
| 23 | Tabela comparativa de MAE |
| 25 | Gráfico Previsão vs Real (scatter plot) |
| 27 | Comparação visual de MAE entre modelos |

---

### 5. Demonstração ao Vivo (3 min)

#### Passo a passo:

1. **Abra o frontend:** `http://localhost:8501`

2. **Preencha um diamante de exemplo:**
   | Campo | Valor |
   |-------|-------|
   | Carat | 1.0 |
   | Cut | Ideal |
   | Color | G |
   | Clarity | VS1 |
   | Depth | 61.5 |
   | Table | 55.0 |
   | X | 6.5 |
   | Y | 6.5 |
   | Z | 4.0 |

3. **Clique em "Prever"** → Veja o preço estimado (~$6.500)

4. **Experimente:** Mude o Carat para **2.0** → Preço sobe para ~$16.000!

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos
```bash
pip install -r requirements.txt
```

### Iniciar a API (Terminal 1)
```bash
cd IaModel
python src/api.py
```
> API rodando em: `http://127.0.0.1:8005`

### Iniciar o Frontend (Terminal 2)
```bash
cd IaModel
streamlit run src/frontend.py
```
> Frontend rodando em: `http://localhost:8501`

### API em Produção (Railway)
```
https://web-production-94f5d.up.railway.app/predict
```

---

## ✅ Checklist de Verificação

- [ ] Notebook executou no Google Colab sem erros
- [ ] Modelos baixados na pasta `models/`
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] API iniciada e respondendo em `/`
- [ ] Frontend carregando corretamente
- [ ] Previsão funcionando (teste com valores acima)

---

## ❓ FAQ - Perguntas Frequentes

| Pergunta | Resposta |
|----------|----------|
| Quantos dados foram usados? | **53.940 diamantes** |
| Por que `random_state=42`? | Garante **reprodutibilidade** dos resultados |
| O que é Dropout? | Técnica que **desliga 20% dos neurônios** aleatoriamente para evitar overfitting |
| O que é Voting/Ensemble? | Combina previsões: `(pred1 + pred2) / 2` para maior estabilidade |
| Qual fator mais influencia o preço? | **Carat** com correlação de **0.92** |
| Por que dois modelos? | Um simples e um com regularização - ensemble melhora a precisão |

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia |
|-----------|------------|
| **ML Framework** | TensorFlow / Keras |
| **API** | FastAPI + Uvicorn |
| **Frontend** | Streamlit |
| **Data Processing** | Pandas, Scikit-learn |
| **Visualização** | Plotly, Seaborn |
| **Deploy** | Railway |

---

## 👥 Equipe

*Adicione os nomes dos integrantes aqui*

---

> 💎 *"A IA não substitui o especialista, mas o capacita a tomar decisões mais rápidas e consistentes."*

