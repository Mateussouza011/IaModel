# Plano de Implementação - Frontend Streamlit

## Objetivo
Criar uma interface gráfica amigável para consumir a API de previsão de custos de seguro e visualizar os dados de treinamento.

## Mudanças Propostas

### Frontend
#### [NEW] [frontend.py](file:///c:/Users/mateu/IaModel/frontend.py)
- **Framework**: Streamlit.
- **Funcionalidades**:
    1.  **Dashboard de Dados**: Aba para visualizar o dataset de treino (`insurance.csv`).
    2.  **Simulador de Custos**: Formulário interativo para enviar dados para a API.
- **UX Improvements**:
    - `age`: Slider (18-100).
    - `bmi`: Slider (10-60).
    - `children`: Slider/Select (0-10).
    - `sex`, `smoker`, `region`: Dropdowns (Selectbox) com opções claras.
    - **Visualização**: Mostrar o resultado com destaque (Metrics) e talvez um gráfico comparativo.

### Configuração
#### [MODIFY] [requirements.txt](file:///c:/Users/mateu/IaModel/requirements.txt)
- Adicionar `streamlit` e `requests`.

## Verificação
- Rodar a API em um terminal: `uvicorn app:app --reload`
- Rodar o Streamlit em outro: `streamlit run frontend.py`
- Verificar se a predição funciona e se os dados são exibidos corretamente.
