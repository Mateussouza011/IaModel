# Plano de Otimização do Modelo

## Objetivo
Aumentar a precisão (R2 Score) do modelo de previsão de custos. Atualmente em ~0.87. Meta: > 0.89.

## Estratégia
1.  **Feature Engineering**:
    - Adicionar `PolynomialFeatures(degree=2)` para capturar interações importantes (ex: Fumante * BMI é um fator crítico no custo de seguro).
2.  **Otimização de Hiperparâmetros**:
    - Utilizar `GridSearchCV` ou parâmetros mais robustos para `RandomForest` e `GradientBoosting`.
3.  **Correção de Frontend**:
    - Ajustar `use_container_width` para remover warnings.

## Mudanças
### [MODIFY] [train_model.py](file:///c:/Users/mateu/IaModel/train_model.py)
- Incluir `PolynomialFeatures` no pipeline.
- Aumentar `n_estimators` e ajustar `max_depth`.

### [MODIFY] [frontend.py](file:///c:/Users/mateu/IaModel/frontend.py)
- Substituir `use_container_width` por `width` onde aplicável (ou apenas remover se for deprecated warning falso positivo, mas o log diz para substituir).

## Execução
- Rodar `python train_model.py`.
- Reiniciar API.
