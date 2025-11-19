import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# 1. Carregamento dos Dados
print("Carregando dados...")
url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
df = pd.read_csv(url)

# 2. Pré-processamento
print("Pré-processando...")
X = df.drop('charges', axis=1)
y = df['charges']

categorical_features = ['sex', 'smoker', 'region']
numerical_features = ['age', 'bmi', 'children']

# Pipeline numérico com PolynomialFeatures para capturar interações (ex: Fumante * BMI)
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('poly', PolynomialFeatures(degree=2, include_bias=False))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numerical_features),
        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_features)
    ])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Definição dos Modelos Base
rf = RandomForestRegressor(random_state=42)
gb = GradientBoostingRegressor(random_state=42)

# 4. Otimização de Hiperparâmetros (GridSearch Simplificado para não demorar muito)
print("Otimizando Random Forest...")
param_grid_rf = {
    'model__n_estimators': [100, 200],
    'model__max_depth': [None, 10, 20],
    'model__min_samples_split': [2, 5]
}
pipeline_rf = Pipeline(steps=[('preprocessor', preprocessor), ('model', rf)])
grid_rf = GridSearchCV(pipeline_rf, param_grid_rf, cv=3, n_jobs=-1, scoring='r2')
grid_rf.fit(X_train, y_train)
best_rf = grid_rf.best_estimator_.named_steps['model']
print(f"Melhor RF: {grid_rf.best_params_}")

print("Otimizando Gradient Boosting...")
param_grid_gb = {
    'model__n_estimators': [100, 200],
    'model__learning_rate': [0.05, 0.1],
    'model__max_depth': [3, 5]
}
pipeline_gb = Pipeline(steps=[('preprocessor', preprocessor), ('model', gb)])
grid_gb = GridSearchCV(pipeline_gb, param_grid_gb, cv=3, n_jobs=-1, scoring='r2')
grid_gb.fit(X_train, y_train)
best_gb = grid_gb.best_estimator_.named_steps['model']
print(f"Melhor GB: {grid_gb.best_params_}")

# 5. Voting Regressor com os Melhores Modelos
print("Treinando Voting Regressor Otimizado...")
voting_model = VotingRegressor(estimators=[
    ('rf', best_rf),
    ('gb', best_gb)
])

final_pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', voting_model)])
final_pipeline.fit(X_train, y_train)

# 6. Avaliação
print("Avaliando...")
y_pred = final_pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R2 Score: {r2:.4f}")

# 7. Salvar o Modelo
import os
model_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models')
os.makedirs(model_dir, exist_ok=True)
model_filename = os.path.join(model_dir, 'voting_model.joblib')
joblib.dump(final_pipeline, model_filename)
print(f"Modelo otimizado salvo em {model_filename}")
