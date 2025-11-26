# 💎 Previsão de Preço de Diamantes com Inteligência Artificial
## Guia de Apresentação para Leigos

---

# 📋 ROTEIRO DA APRESENTAÇÃO

Use este documento como guia para sua apresentação. Cada seção indica **o que falar** e **o que mostrar na tela**.

---

## 🎯 PARTE 1: INTRODUÇÃO (2-3 minutos)

### O que você deve explicar:

**Comece com uma pergunta:**
> "Vocês já se perguntaram como as joalherias sabem o preço de um diamante?"

**Explique o problema de forma simples:**
- Cada diamante é único (peso, cor, clareza, corte, tamanho)
- Precificar manualmente é demorado e pode ter erros humanos
- **Nossa solução:** Criamos um "cérebro artificial" que aprende a precificar diamantes automaticamente

### 📍 ONDE MOSTRAR:

| O que mostrar | Onde está | Como abrir |
|---------------|-----------|------------|
| Interface funcionando | `src/frontend.py` | Terminal: `streamlit run src/frontend.py` |
| Fazer previsão rápida | Navegador: `http://localhost:8501` | Preencha os campos e clique "Prever" |

---

## 📊 PARTE 2: OS DADOS (3-4 minutos)

### O que você deve explicar:

**De onde vieram os dados:**
- Usamos um banco de dados famoso chamado "Diamonds Dataset"
- Contém informações de **mais de 53.000 diamantes reais**
- Cada diamante tem 9 características que influenciam o preço

**As 9 características do diamante:**

| Característica | O que significa | Exemplo |
|----------------|-----------------|---------|
| **Carat** (Quilate) | Peso do diamante | 0.5, 1.0, 2.0 quilates |
| **Cut** (Corte) | Qualidade do corte | Fair, Good, Very Good, Premium, Ideal |
| **Color** (Cor) | Quão "branquinho" é | D (melhor) até J (pior) |
| **Clarity** (Clareza) | Se tem "manchinhas" dentro | IF (perfeito) até I1 (visíveis) |
| **Depth** (Profundidade) | Altura do diamante | Porcentagem |
| **Table** (Mesa) | Largura do topo | Porcentagem |
| **X, Y, Z** | Dimensões em milímetros | Largura, altura, profundidade |

**Divisão dos dados para treino:**
- **80% para treinar** (~42.000 diamantes) → a IA "estuda" esses
- **20% para testar** (~11.000 diamantes) → usamos para verificar se ela aprendeu

### 📍 ONDE MOSTRAR:

| O que mostrar | Onde está no Notebook | Célula |
|---------------|----------------------|--------|
| Primeiros diamantes | `df.head(10)` | Seção 1 - 3ª célula |
| Total de diamantes | `print(f"Total de diamantes: {len(df):,}")` | Seção 1 - 3ª célula |
| Estatísticas | `df.describe()` | Seção 1 - 4ª célula |
| Valores nulos | `df.isnull().sum()` | Seção 1 - 6ª célula |
| Divisão treino/teste | `train_test_split(X, y, test_size=0.2, random_state=42)` | Seção 3 - 1ª célula de código |
| Embaralhamento (random_state=42) | Mesma linha acima | Seção 3 - 1ª célula de código |

**🖼️ GRÁFICOS PARA MOSTRAR:**

| Gráfico | Onde está no Notebook | O que explicar |
|---------|----------------------|----------------|
| Histograma de Preços | Seção 2.1 - 1ª célula | "Maioria dos diamantes custa menos de $5.000" |
| Boxplot de Preços | Seção 2.1 - 1ª célula | "Os pontos fora são diamantes muito caros (outliers)" |
| Distribuição por Corte/Cor/Clareza | Seção 2.2 - 1ª célula | "Ideal é o corte mais comum no dataset" |
| Preço Médio por Categoria | Seção 2.3 - 1ª célula | "Curiosamente, corte 'Fair' tem preço médio maior (por causa do peso)" |
| Matriz de Correlação | Seção 2.4 - 1ª célula | "Carat tem correlação 0.92 com preço - é o fator mais importante!" |
| Carat vs Preço (scatter) | Seção 2.5 - 1ª célula | "Quanto maior o quilate, maior o preço" |
| Distribuição das variáveis numéricas | Seção 2.6 - 1ª célula | "Mostra como cada característica se distribui" |

---

## 🧠 PARTE 3: A INTELIGÊNCIA ARTIFICIAL (5-6 minutos)

### O que você deve explicar:

**O que é uma Rede Neural (analogia simples):**
> "Imaginem o cérebro humano: ele tem bilhões de neurônios conectados que aprendem com experiência. Nossa IA funciona de forma parecida, mas com neurônios virtuais."

**O que é um problema de Regressão:**
> "Nosso problema é de regressão porque queremos prever um número (o preço em dólares). Se fosse para classificar como 'barato' ou 'caro', seria classificação."

**Como ela aprende:**
1. Mostramos um diamante com o preço real
2. A IA tenta "chutar" o preço
3. Calculamos o quanto ela errou
4. Ela ajusta seus "neurônios" para errar menos
5. Repetimos isso milhares de vezes (50 épocas)

### 📍 ONDE MOSTRAR:

| O que mostrar | Onde está no Notebook | Célula |
|---------------|----------------------|--------|
| Arquitetura Modelo 1 | `model1_temp.summary()` | Seção 4 - 1ª célula de código |
| Arquitetura Modelo 2 | `model2_temp.summary()` | Seção 4 - 1ª célula de código |
| Épocas (50) | `epochs=50` | Seção 4 - 2ª célula de código |
| Batch Size (32) | `batch_size=32` | Seção 4 - 2ª célula de código |
| Validation Split (20%) | `validation_split=0.2` | Seção 4 - 2ª célula de código |
| Dropout (20%) | `layers.Dropout(0.2)` | Seção 4 - 1ª célula (create_model_2) |
| Função de Erro (MAE) | `loss='mae'` | Seção 4 - 1ª célula (model.compile) |

---

### 🔢 NÚMEROS TÉCNICOS IMPORTANTES (decore estes!)

| Parâmetro | Valor | Onde está | O que significa |
|-----------|-------|-----------|-----------------|
| **Épocas** | 50 | `epochs=50` | A IA "estudou" todos os diamantes 50 vezes |
| **Batch Size** | 32 | `batch_size=32` | Estuda 32 diamantes de cada vez |
| **Dados de Treino** | ~42.000 | Output da célula | 80% dos 53.000 diamantes |
| **Dados de Teste** | ~11.000 | Output da célula | 20% dos 53.000 diamantes |
| **Validation Split** | 20% | `validation_split=0.2` | Parte do treino para validar |
| **Random State** | 42 | `random_state=42` | Semente para reproduzir resultados |
| **Input Shape** | 26 | Output: `Input Shape: 26` | Features após pré-processamento |

---

### 🏗️ ARQUITETURA DOS MODELOS

### 📍 ONDE MOSTRAR A ARQUITETURA:

**No Notebook - Seção 4, 1ª célula de código:**

```
Modelo 1 (Simples):
┌─────────────────────┐
│ dense (Dense)       │  → 64 neurônios
├─────────────────────┤
│ dense_1 (Dense)     │  → 32 neurônios  
├─────────────────────┤
│ dense_2 (Dense)     │  → 1 neurônio (saída = preço)
└─────────────────────┘

Modelo 2 (Com Dropout):
┌─────────────────────┐
│ dense_3 (Dense)     │  → 128 neurônios
├─────────────────────┤
│ dropout (Dropout)   │  → 20% desligados
├─────────────────────┤
│ dense_4 (Dense)     │  → 64 neurônios
├─────────────────────┤
│ dense_5 (Dense)     │  → 32 neurônios
├─────────────────────┤
│ dense_6 (Dense)     │  → 1 neurônio (saída = preço)
└─────────────────────┘
```

**O que explicar:**
> "É como pedir opinião para dois especialistas diferentes e fazer a média. Se um errar muito, o outro compensa. Isso se chama Voting Ensemble."

---

### 📍 GRÁFICOS DE TREINAMENTO (Seção 4.1):

| Gráfico | O que mostra | O que explicar |
|---------|--------------|----------------|
| Histórico Modelo 1 | Linha azul (treino) e vermelha (validação) | "O erro vai diminuindo a cada época" |
| Histórico Modelo 2 | Linha azul (treino) e vermelha (validação) | "Se as linhas se afastam muito = overfitting" |

---

## 📊 PARTE 4: RESULTADOS (3-4 minutos)

### 📍 ONDE MOSTRAR OS RESULTADOS:

| O que mostrar | Onde está no Notebook | Célula |
|---------------|----------------------|--------|
| MAE Modelo 1 | `print(f"Modelo 1 MAE: ${mae1:,.2f}")` | Seção 5 - 1ª célula |
| MAE Modelo 2 | `print(f"Modelo 2 MAE: ${mae2:,.2f}")` | Seção 5 - 1ª célula |
| MAE Voting | `print(f"Voting Ensemble MAE: ${mae_voting:,.2f}")` | Seção 5 - 1ª célula |
| Melhor modelo | Mensagem "🏆 O ... teve o melhor desempenho!" | Seção 5 - 1ª célula |

### 📍 GRÁFICOS DE RESULTADOS:

| Gráfico | Seção | O que explicar |
|---------|-------|----------------|
| Previsão vs Real (3 gráficos) | Seção 5.1 | "Quanto mais perto da linha vermelha, melhor a previsão" |
| Distribuição dos Erros | Seção 5.2 | "A maioria dos erros está perto de zero (centro)" |
| Comparação de MAE (barras) | Seção 5.3 | "Mostra qual modelo errou menos em média" |

---

## ⚡ PARTE 5: O SISTEMA EM PRODUÇÃO (3-4 minutos)

### 📍 ONDE MOSTRAR CADA ARQUIVO:

| Componente | Arquivo | Como abrir no VS Code |
|------------|---------|----------------------|
| Notebook de Treino | `notebooks/train_diamonds_colab.ipynb` | Duplo clique no arquivo |
| API | `src/api.py` | Duplo clique no arquivo |
| Frontend | `src/frontend.py` | Duplo clique no arquivo |
| Modelos treinados | `models/model1.keras` | Apenas mencione (arquivo binário) |
| Pré-processador | `models/preprocessor.joblib` | Apenas mencione (arquivo binário) |

### 📍 ONDE MOSTRAR A API:

| O que mostrar | URL | Como chegar |
|---------------|-----|-------------|
| Documentação da API | `http://localhost:8000/docs` | Abra no navegador |
| Testar endpoint | Clique em `/predict` → "Try it out" | Preencha os dados e execute |
| Ver resposta JSON | Resultado aparece abaixo | Mostra as 3 previsões |

### 📍 ONDE MOSTRAR O FRONTEND:

| O que mostrar | URL | Como chegar |
|---------------|-----|-------------|
| Interface visual | `http://localhost:8501` | Abra no navegador |
| Campos de entrada | Lado esquerdo da tela | Sliders e dropdowns |
| Botão de previsão | Abaixo dos campos | Clique para prever |
| Resultados | Centro da tela | Mostra os 3 preços |

---

## 🎬 PARTE 6: DEMONSTRAÇÃO AO VIVO (3-5 minutos)

### 📍 PASSO A PASSO COM LOCAIS EXATOS:

**Passo 1 - Abrir o Frontend:**
```
Navegador → http://localhost:8501
```

**Passo 2 - Preencher dados de teste:**

| Campo | Valor | Onde está na tela |
|-------|-------|-------------------|
| Carat | 1.0 | Primeiro slider |
| Cut | Ideal | Primeiro dropdown |
| Color | G | Segundo dropdown |
| Clarity | VS1 | Terceiro dropdown |
| Depth | 61.5 | Segundo slider |
| Table | 55.0 | Terceiro slider |
| X | 6.5 | Quarto slider |
| Y | 6.5 | Quinto slider |
| Z | 4.0 | Sexto slider |

**Passo 3 - Clicar em "Prever":**
```
Botão azul abaixo dos campos
```

**Passo 4 - Mostrar resultados:**
```
Centro da tela - aparece:
- Previsão Modelo 1: $X,XXX
- Previsão Modelo 2: $X,XXX  
- Previsão Final (Voting): $X,XXX
```

**Passo 5 - Mudar valores e mostrar impacto:**

| Mudança | Efeito esperado |
|---------|-----------------|
| Carat: 1.0 → 2.0 | Preço sobe MUITO (carat é o fator mais importante) |
| Cut: Ideal → Fair | Preço cai um pouco |
| Clarity: VS1 → I1 | Preço cai |

---

## 📍 RESUMO: MAPA COMPLETO DO QUE MOSTRAR

### NO NOTEBOOK (Google Colab):

| Seção | O que tem | O que falar |
|-------|-----------|-------------|
| **1** | Carregamento dos dados | "53.000 diamantes, 9 características" |
| **2.1** | Histograma/Boxplot de preços | "Maioria custa menos de $5.000" |
| **2.2** | Distribuição categóricas | "Ideal é o corte mais comum" |
| **2.3** | Preço médio por categoria | "Corte 'Fair' tem preço alto por causa do peso" |
| **2.4** | Matriz de correlação | "Carat tem 0.92 de correlação com preço!" |
| **2.5** | Scatter Carat vs Preço | "Relação direta entre peso e preço" |
| **2.6** | Distribuição numéricas | "Como cada variável se distribui" |
| **3** | Pré-processamento | "80% treino, 20% teste, random_state=42" |
| **4** | Arquitetura dos modelos | "64→32→1 vs 128→dropout→64→32→1" |
| **4** | Treinamento | "50 épocas, batch 32" |
| **4.1** | Gráficos de treinamento | "Erro diminui a cada época" |
| **5** | Resultados MAE | "Erro médio em dólares" |
| **5.1** | Previsão vs Real | "Pontos na linha = previsão perfeita" |
| **5.2** | Distribuição de erros | "Maioria dos erros perto de zero" |
| **5.3** | Comparação de MAE | "Qual modelo foi melhor" |
| **6** | Salvar modelos | "Exporta para usar na API" |
| **7** | Teste de carregamento | "Verifica se os modelos funcionam" |

### NA API (`http://localhost:8000/docs`):

| Endpoint | O que mostrar |
|----------|---------------|
| `/predict` | Enviar dados e receber previsões |
| `/health` | Verificar se está funcionando |

### NO FRONTEND (`http://localhost:8501`):

| Parte da tela | O que mostrar |
|---------------|---------------|
| Sidebar (esquerda) | Campos de entrada |
| Centro | Resultados das previsões |
| Botão "Prever" | Fazer a previsão |

---

## ❓ PERGUNTAS FREQUENTES E ONDE MOSTRAR A RESPOSTA

| Pergunta | Onde mostrar a resposta |
|----------|------------------------|
| "Quantos dados usou?" | Notebook Seção 1: `len(df)` = 53.940 |
| "Qual o erro médio?" | Notebook Seção 5: MAE em dólares |
| "Por que 42?" | Notebook Seção 3: `random_state=42` |
| "O que é Dropout?" | Notebook Seção 4: `layers.Dropout(0.2)` |
| "Como funciona o Voting?" | Notebook Seção 5: `(pred1 + pred2) / 2` |
| "Qual fator mais importante?" | Notebook Seção 2.4: Correlação Carat = 0.92 |

---

## 📁 ESTRUTURA DO PROJETO

```
IaModel/
├── models/                              # Modelos treinados
│   ├── model1.keras                     # Modelo 1 (simples)
│   ├── model2.keras                     # Modelo 2 (com dropout)
│   └── preprocessor.joblib              # Pré-processador de dados
├── notebooks/
│   └── train_diamonds_colab.ipynb       # Notebook de treino (Google Colab)
├── src/
│   ├── api.py                           # API REST do sistema
│   └── frontend.py                      # Interface visual
├── scripts/
│   ├── run_api.bat                      # Inicia a API
│   └── run_frontend.bat                 # Inicia a interface
├── PRESENTATION.md                      # Este guia de apresentação
└── requirements.txt                     # Dependências do projeto
```

---

## 🚀 COMO RODAR O PROJETO

**1. Treinar os modelos (Google Colab):**
- Faça upload do notebook para o Google Colab
- Execute todas as células
- Baixe os arquivos `model1.keras`, `model2.keras` e `preprocessor.joblib`
- Coloque na pasta `models/`

**2. Iniciar a API:**
```bash
cd src
python -m uvicorn api:app --reload
```

**3. Iniciar o Frontend:**
```bash
cd src
streamlit run frontend.py
```

---

## 🎯 CHECKLIST PRÉ-APRESENTAÇÃO

- [ ] Notebook rodou sem erros no Colab
- [ ] Modelos baixados e na pasta `models/`
- [ ] API iniciada e funcionando (`localhost:8000/docs`)
- [ ] Frontend iniciado e funcionando (`localhost:8501`)
- [ ] Testei uma previsão e funcionou
- [ ] Tenho prints/vídeo de backup caso falhe
- [ ] Decorei os números: 53.000, 42.000, 50 épocas, 32 batch

---

**Boa apresentação! 💎🚀**

