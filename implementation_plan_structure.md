# Plano de Reestruturação e Polimento

## Objetivo
Profissionalizar o projeto organizando a estrutura de arquivos, melhorando a interface do usuário (UI/UX) e criando um documento de apresentação.

## 1. Reestruturação de Pastas
Organizar a raiz do projeto para separar código fonte, modelos e documentação.

**Estrutura Proposta:**
```
IaModel/
├── src/                  # Código Fonte
│   ├── api.py            # (Antigo app.py)
│   ├── frontend.py       # Interface Streamlit
│   └── train_model.py    # Script de treinamento
├── models/               # Artefatos do Modelo
│   └── voting_model.joblib
├── notebooks/            # Notebooks Jupyter
│   └── notebook_regressao.ipynb
├── scripts/              # Scripts de Automação
│   ├── run_api.bat
│   └── run_frontend.bat
├── assets/               # Imagens/Logos (se houver)
├── requirements.txt
└── PRESENTATION.md       # Plano de Apresentação
```

## 2. Melhoria Visual (Frontend)
- **Design System**: Aplicar CSS customizado para cards, métricas e botões.
- **Layout**: Usar `st.sidebar` para configurações e filtros.
- **Gráficos**: Substituir gráficos nativos simples por `plotly` (interativos).
- **Feedback**: Melhorar mensagens de sucesso/erro.

## 3. Plano de Apresentação (PRESENTATION.md)
Criar um documento markdown detalhando:
- O Problema (Custos de Seguro).
- A Solução (IA + App Web).
- Tecnologias (FastAPI, Streamlit, Scikit-learn).
- Como Executar.

## Passos de Execução
1.  **Criar Pastas**: `src`, `models`, `notebooks`, `scripts`.
2.  **Mover e Renomear Arquivos**:
    - `app.py` -> `src/api.py`
    - `frontend.py` -> `src/frontend.py`
    - `train_model.py` -> `src/train_model.py`
    - `voting_model.joblib` -> `models/voting_model.joblib` (será regerado)
    - `notebook_regressao.ipynb` -> `notebooks/...`
3.  **Atualizar Código**:
    - `src/train_model.py`: Salvar em `../models/`.
    - `src/api.py`: Carregar de `../models/`.
    - `src/frontend.py`: Atualizar URL (porta 8005 mantida) e aplicar novo design.
4.  **Retreinar Modelo**: Executar `src/train_model.py` para gerar o modelo otimizado na nova pasta.
5.  **Atualizar Scripts**: Ajustar caminhos nos `.bat`.
6.  **Criar Apresentação**: Escrever `PRESENTATION.md`.
