# Previsão de Preço de Diamantes com IA

## Estrutura do Projeto

```
IaModel/
├── models/                     → Modelos treinados
├── notebooks/
│   └── treinamentoPredictDiamantes.ipynb
├── src/
│   ├── api.py                  → API REST
│   └── frontend.py             → Interface
└── scripts/
```

---

## Roteiro da Apresentação

### 1. Introdução (2 min)

> "Criamos uma IA que aprende a precificar diamantes automaticamente."

**Mostre:** `http://localhost:8501`

---

### 2. Os Dados (3 min)

| Característica | Significado |
|----------------|-------------|
| Carat | Peso (quilates) |
| Cut | Qualidade do corte |
| Color | Cor (D=melhor → J=pior) |
| Clarity | Clareza interna |
| X, Y, Z | Dimensões (mm) |

**Números:** 53.940 diamantes | 80% treino / 20% teste | 9 características

**Notebook:**

| Célula | Conteúdo |
|--------|----------|
| 5 | Primeiros dados |
| 6 | Estatísticas |
| 10 | Histograma e Boxplot |
| 12 | Matriz de correlação |
| 14 | Scatter Carat vs Preço |

---

### 3. A IA (5 min)

> "Redes neurais - como um cérebro artificial que aprende com exemplos."

| Parâmetro | Valor |
|-----------|-------|
| Épocas | 50 |
| Batch Size | 32 |
| Validation | 20% |

**Arquitetura:**
- Modelo 1: 64 → 32 → 1
- Modelo 2: 128 → Dropout(20%) → 64 → 32 → 1

**Notebook:**

| Célula | Conteúdo |
|--------|----------|
| 16 | Pré-processamento |
| 18 | Definição dos modelos |
| 19 | Treinamento |
| 21 | Histórico de treino |

---

### 4. Resultados (3 min)

> "MAE = Erro Médio Absoluto em dólares."

**Notebook:**

| Célula | Conteúdo |
|--------|----------|
| 23 | Tabela MAE |
| 25 | Gráfico Previsão vs Real |
| 27 | Comparação de MAE |

---

### 5. Demo (3 min)

1. Abra `http://localhost:8501`
2. Preencha: Carat=1.0, Cut=Ideal, Color=G, Clarity=VS1
3. Clique "Prever"
4. Mude Carat para 2.0 → veja o preço subir

---

## Como Rodar

```bash
# API
cd src && python -m uvicorn api:app --reload --port 8000

# Frontend
cd src && streamlit run frontend.py
```

---

## Checklist

- [ ] Notebook executou no Colab
- [ ] Modelos baixados em `models/`
- [ ] API e Frontend rodando
- [ ] Previsão funcionando

---

## FAQ

| Pergunta | Resposta |
|----------|----------|
| Quantos dados? | 53.940 |
| Por que 42? | Reprodutibilidade |
| O que é Dropout? | Desliga 20% dos neurônios |
| Voting? | (pred1 + pred2) / 2 |
| Fator principal? | Carat (correlação 0.92) |

