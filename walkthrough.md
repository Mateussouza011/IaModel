# Walkthrough - Desafio de Regressão e API

Este documento descreve a solução implementada para o desafio de regressão, utilizando o dataset de custos de seguro médico.

## Artefatos Entregues

| Arquivo | Descrição |
| :--- | :--- |
| [notebook_regressao.ipynb](file:///c:/Users/mateu/IaModel/notebook_regressao.ipynb) | Notebook Jupyter completo na pasta IaModel. |
| [app.py](file:///c:/Users/mateu/IaModel/app.py) | API FastAPI. |
| [frontend.py](file:///c:/Users/mateu/IaModel/frontend.py) | Aplicação Web Streamlit (Dashboard + Simulador). |
| [voting_model.joblib](file:///c:/Users/mateu/IaModel/voting_model.joblib) | Modelo treinado e serializado. |
| [requirements.txt](file:///c:/Users/mateu/IaModel/requirements.txt) | Lista de dependências. |

## Como Usar

### 1. Instalação
Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

### 2. Executar a API (Backend)
Em um terminal, inicie o servidor da API:
```bash
python app.py
```
A API ficará disponível em `http://localhost:8005`.

### 3. Executar o Frontend (Streamlit)
Em **outro terminal**, inicie a aplicação Streamlit:
```bash
python -m streamlit run frontend.py
```
O navegador abrirá automaticamente (geralmente em `http://localhost:8501`).

### 4. Usando a Aplicação
1.  **Simulador de Custos**: Na primeira aba, ajuste os sliders (Idade, IMC, Filhos) e selecione as opções (Gênero, Fumante, Região). Clique em "Calcular Previsão" para ver o custo estimado.
2.  **Dados de Treinamento**: Na segunda aba, explore o dataset original, filtre por fumantes e veja estatísticas básicas.

## Resultados da Validação
- **Modelo**: Voting Regressor (Random Forest + Gradient Boosting).
- **Performance (Teste)**: R2 Score ~0.87.
- **Integração**: Frontend conecta-se à API local para realizar inferências em tempo real.
