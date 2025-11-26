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

**O que mostrar:**
- Abra o navegador e mostre a interface do sistema funcionando (`frontend.py`)
- Faça uma previsão rápida para impressionar a audiência

---

## 📊 PARTE 2: OS DADOS (3-4 minutos)
### O que você deve explicar:

**De onde vieram os dados:**
- Usamos um banco de dados chamado "Diamonds Dataset"
- Contém informações de **mais de 53.000 diamantes**
- Cada diamante tem 9 características que influenciam o preço

**As 9 características do diamante (explique de forma simples):**

| Característica | O que significa | Exemplo |
|---------------|-----------------|---------|
| **Carat** (Quilate) | Peso do diamante | 0.5, 1.0, 2.0 quilates |
| **Cut** (Corte) | Qualidade do corte | Fair, Good, Very Good, Premium, Ideal |
| **Color** (Cor) | Quão "branquinho" é | D (melhor) até J (pior) |
| **Clarity** (Clareza) | Se tem "manchinhas" dentro | IF (perfeito) até I1 (visíveis) |
| **Depth** (Profundidade) | Altura do diamante | Porcentagem |
| **Table** (Mesa) | Largura do topo | Porcentagem |
| **X, Y, Z** | Dimensões em mm | Largura, altura, profundidade |

**Divisão dos dados para treino:**
- **80% para treinar** (~42.000 diamantes) → a IA "estuda" esses
- **20% para testar** (~11.000 diamantes) → usamos para ver se ela aprendeu

**O que mostrar:**
- Abra o notebook (`notebooks/train_diamonds_colab.ipynb`)
- Mostre o `df.head()` com os primeiros diamantes
- Se possível, mostre alguns gráficos de distribuição

---

## 🧠 PARTE 3: A INTELIGÊNCIA ARTIFICIAL (5-6 minutos)
### O que você deve explicar:

**O que é uma Rede Neural (analogia simples):**
> "Imaginem o cérebro humano: ele tem bilhões de neurônios conectados que aprendem com experiência. Nossa IA funciona de forma parecida, mas com neurônios virtuais."

**Como ela aprende:**
1. Mostramos um diamante com o preço real
2. A IA tenta "chutar" o preço
3. Calculamos o quanto ela errou
4. Ela ajusta seus "neurônios" para errar menos
5. Repetimos isso milhares de vezes

---

### 🔢 NÚMEROS TÉCNICOS IMPORTANTES (decore estes!)

| Parâmetro | Valor | O que significa (versão simples) |
|-----------|-------|----------------------------------|
| **Épocas** | 50 | A IA "estudou" todos os diamantes 50 vezes |
| **Batch Size** | 32 | Estuda 32 diamantes de cada vez |
| **Dados de Treino** | ~42.000 | Quantidade de diamantes para aprender |
| **Dados de Teste** | ~11.000 | Quantidade para verificar se aprendeu |
| **Taxa de Aprendizado** | Automática (Adam) | Velocidade que ela aprende |

---

### 🏗️ ARQUITETURA DOS MODELOS (versão simples)

**Por que usamos 2 modelos?**
> "É como pedir opinião para dois especialistas diferentes e fazer a média. Se um errar muito, o outro compensa."

**Modelo 1 - O Simples:**
```
Entrada (9 características)
    ↓
64 neurônios → 32 neurônios → Preço
```
- Pensa de forma direta e objetiva
- Bom para casos "normais"

**Modelo 2 - O Cuidadoso:**
```
Entrada (9 características)
    ↓
128 neurônios → [Dropout 20%] → 64 neurônios → 32 neurônios → Preço
```
- Mais detalhista
- Tem "Dropout": durante o treino, "desliga" 20% dos neurônios aleatoriamente
- **Por que Dropout?** Evita que a IA "decore" ao invés de "aprender"

**Previsão Final:**
```
Preço Final = (Previsão Modelo 1 + Previsão Modelo 2) ÷ 2
```

---

### 📉 FUNÇÃO DE ERRO: MAE (Erro Médio Absoluto)

**O que é MAE?**
> "É a média de quanto a IA erra em dólares. Se o MAE é 300, significa que em média ela erra $300 para mais ou para menos."

**Por que escolhemos MAE?**
- Fácil de entender (está em dólares!)
- Não pune demais diamantes muito caros ou muito baratos

**O que mostrar:**
- Mostre o código do modelo em `src/train_diamonds.py`
- Aponte para os números: epochs=50, batch_size=32
- Se tiver os resultados, mostre o MAE final

---

## ⚡ PARTE 4: O SISTEMA EM PRODUÇÃO (3-4 minutos)
### O que você deve explicar:

**Como transformamos a IA em um serviço web:**

```
Usuário → Interface (Frontend) → API → Modelos de IA → Resposta com preço
```

**Componentes do sistema:**

| Componente | Arquivo | O que faz |
|------------|---------|-----------|
| **API** | `src/api.py` | Recebe pedidos e retorna previsões |
| **Frontend** | `src/frontend.py` | Tela bonita para o usuário |
| **Modelos** | `models/*.keras` | O "cérebro" treinado |
| **Pré-processador** | `models/preprocessor.joblib` | Prepara os dados para a IA |

**Tecnologias usadas (mencione rapidamente):**
- **Python**: Linguagem de programação principal
- **TensorFlow/Keras**: Biblioteca para criar redes neurais
- **FastAPI**: Framework para criar a API web
- **Streamlit ou Gradio**: Interface visual amigável

**O que mostrar:**
- Execute `scripts/run_api.bat` e mostre a API funcionando
- Execute `scripts/run_frontend.bat` e mostre a interface
- Faça uma previsão ao vivo!

---

## 🎬 PARTE 5: DEMONSTRAÇÃO AO VIVO (3-5 minutos)
### Passo a passo da demo:

1. **Abra a interface** do frontend
2. **Preencha os dados** de um diamante fictício:
   - Carat: 1.0
   - Cut: Ideal
   - Color: G
   - Clarity: VS1
   - Depth: 61.5
   - Table: 55.0
   - X: 6.5, Y: 6.5, Z: 4.0
3. **Clique em "Prever"**
4. **Mostre o resultado** e explique:
   - Previsão do Modelo 1
   - Previsão do Modelo 2
   - Média final
5. **Mude alguns valores** e mostre como o preço muda

---

## ❓ PARTE 6: PERGUNTAS FREQUENTES (tenha estas respostas prontas)

**"A IA sempre acerta?"**
> "Não, ela tem uma margem de erro. Em média, erra cerca de X dólares. Mas é muito mais rápida e consistente que uma avaliação manual."

**"E se eu colocar dados errados?"**
> "O sistema valida os dados antes de processar. Se você digitar 'dez' ao invés de '10', ele avisa que está errado."

**"Quanto tempo leva para treinar?"**
> "Com 50 épocas e 42.000 diamantes, leva cerca de 5-10 minutos em um computador comum."

**"Ela funciona para outros produtos?"**
> "Sim! Podemos adaptar para carros, imóveis, qualquer coisa que tenha características mensuráveis e preços históricos."

---

## 📌 RESUMO FINAL (1 minuto)

Termine a apresentação com estes pontos:

✅ **O Problema:** Precificar diamantes é complexo e demorado

✅ **A Solução:** Uma IA que aprende com 53.000 diamantes reais

✅ **A Tecnologia:** Duas redes neurais que "votam" juntas

✅ **O Resultado:** Previsões em menos de 1 segundo

✅ **O Diferencial:** Sistema completo, do treino ao deploy

---

## 🎯 DICAS PARA A APRESENTAÇÃO

1. **Fale devagar** nos termos técnicos
2. **Use analogias** (cérebro, especialistas votando, etc.)
3. **Faça a demo funcionar ANTES** da apresentação
4. **Tenha backup** (prints ou vídeo) caso a demo falhe
5. **Pratique os números técnicos** (50 épocas, 42.000 dados, etc.)
6. **Mantenha contato visual** com a audiência
7. **Termine com impacto** - faça uma previsão ao vivo!

---

## 📁 ARQUIVOS DO PROJETO

```
IaModel/
├── models/                    # Cérebros treinados da IA
│   ├── model1.keras          # Modelo 1 (simples)
│   ├── model2.keras          # Modelo 2 (profundo)
│   └── preprocessor.joblib   # Preparador de dados
├── notebooks/
│   └── train_diamonds_colab.ipynb  # Notebook de treino
├── src/
│   ├── api.py                # API do sistema
│   ├── frontend.py           # Interface visual
│   ├── train_diamonds.py     # Script de treino
│   └── data_loader.py        # Carregador de dados
└── scripts/
    ├── run_api.bat           # Inicia a API
    └── run_frontend.bat      # Inicia a interface
```

---

**Boa apresentação! 💎🚀**

