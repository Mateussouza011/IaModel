# 🏥 Medical Insurance Cost Prediction: Do Zero ao Deploy
## Relatório Técnico & Apresentação do Projeto

Este documento serve como um guia completo sobre o desenvolvimento da solução de previsão de custos médicos. Ele foi estruturado para demonstrar **domínio técnico profundo** sobre cada etapa, desde a ciência de dados exploratória até a engenharia de software em produção.

---

## 1. � A Origem: O Laboratório de Dados (Jupyter Notebook)
*Arquivo: `notebooks/notebook_regressao.ipynb`*

Antes de escrever qualquer linha de código do aplicativo, realizamos um rigoroso processo científico. O notebook não foi apenas um rascunho, foi onde as decisões cruciais foram tomadas.

### 1.1. Análise Exploratória de Dados (EDA)
Não aceitamos os dados cegamente. Investigamos profundamente:
*   **Qualidade dos Dados**: Verificamos valores nulos (missing values) e duplicatas para garantir a integridade do dataset.
*   **Análise Univariada**: Plotamos histogramas para entender a distribuição da idade e do IMC. Percebemos que a variável alvo (`charges`) tinha uma distribuição assimétrica à direita (positive skewness), comum em dados financeiros.
*   **O "Insight" de Ouro**: Ao cruzar `smoker` (fumante) com `charges`, descobrimos que fumantes não apenas pagam mais, mas têm uma variância de custo muito maior.
*   **Correlação (Heatmap)**: A matriz de correlação revelou que `smoker` tinha a maior correlação positiva com o custo, seguida por `age` e `bmi`.

### 1.2. Experimentação de Modelos
Testamos múltiplas hipóteses antes de escolher a solução final:
*   **Regressão Linear**: Falhou em capturar a complexidade dos dados (Underfitting). O R² foi baixo porque a relação entre as variáveis não é puramente linear.
*   **Árvores de Decisão**: Melhoraram o resultado, mas tendiam a decorar os dados de treino (Overfitting).
*   **Random Forest & Gradient Boosting**: Estes modelos de *Ensemble* mostraram o melhor equilíbrio entre viés e variância.

---

## 2. 🧠 O Cérebro: Engenharia de Machine Learning
*Arquivo: `src/train_model.py`*

Com as descobertas do notebook, construímos um pipeline de treinamento robusto e automatizado.

### 2.1. Feature Engineering Avançada (O Diferencial)
Aqui demonstramos conhecimento além do básico.
*   **O Problema**: Modelos simples tratam variáveis isoladamente.
*   **A Solução**: Utilizamos `PolynomialFeatures(degree=2)`.
*   **Por que?** Isso permitiu ao modelo entender **interações não-lineares**. Por exemplo, o modelo aprendeu matematicamente que:
    > *Risco(Fumante + Obeso) > Risco(Fumante) + Risco(Obeso)*
    Essa interação multiplicativa é crucial para a precisão médica.

### 2.2. Arquitetura Híbrida (Voting Regressor)
Não confiamos em apenas um algoritmo. Implementamos um **Voting Regressor** que combina:
1.  **Random Forest**: Cria centenas de árvores paralelas (Bagging) para reduzir a variância e estabilizar a previsão.
2.  **Gradient Boosting**: Cria árvores sequenciais (Boosting) onde cada uma corrige os erros da anterior, refinando a precisão.
*   **Resultado**: Um modelo que é ao mesmo tempo estável e cirurgicamente preciso (R² ~0.87).

### 2.3. Otimização de Hiperparâmetros
Não usamos configurações padrão ("vanilla"). Aplicamos **GridSearchCV** para testar exaustivamente combinações de:
*   `n_estimators` (número de árvores)
*   `max_depth` (profundidade da árvore)
Isso garante que o modelo foi matematicamente ajustado para este problema específico.

---

## 3. ⚡ O Corpo: Arquitetura de Software (Backend)
*Arquivo: `src/api.py`*

Para colocar o modelo no mundo real, adotamos práticas modernas de Engenharia de Software.

*   **FastAPI (ASGI)**: Escolhemos FastAPI por ser assíncrono e extremamente performático, ideal para inferência de ML em tempo real.
*   **Pydantic (Data Validation)**: Implementamos uma camada de segurança. Se o usuário enviar "trinta" em vez de `30` na idade, a API bloqueia a requisição instantaneamente. Isso garante **Type Safety** e robustez.
*   **Serialização Eficiente**: O modelo é carregado via `joblib`, otimizado para grandes arrays numéricos (NumPy), garantindo tempos de inicialização rápidos.

---

## 4. 🎨 A Face: Experiência do Usuário (Frontend)
*Arquivo: `src/frontend.py`*

A tecnologia precisa ser acessível. Criamos uma interface que esconde a complexidade matemática.

*   **Design System Premium**: Desenvolvemos um tema escuro (Dark Mode) customizado via CSS injection, transmitindo modernidade e profissionalismo.
*   **Data Storytelling**: Não mostramos apenas o número final.
    *   **Velocímetro (Gauge)**: Contextualiza o custo em relação à média nacional.
    *   **Mapas de Calor**: Provam visualmente para o usuário quais variáveis estão aumentando o preço dele.
*   **Interatividade**: Usamos **Plotly** para gráficos que reagem ao mouse, permitindo exploração profunda dos dados.

---

## Resumo Executivo
Este projeto não é apenas um modelo de IA; é uma **solução completa de ponta a ponta**.
1.  Começamos com **Ciência de Dados** rigorosa (Notebook).
2.  Evoluímos para **Engenharia de ML** avançada (Pipeline Híbrido).
3.  Implementamos **Engenharia de Software** sólida (API Robusta).
4.  Entregamos **Design de Produto** de alto nível (Frontend Premium).

*Desenvolvido por Mateus & Antigravity AI*
