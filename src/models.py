import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler


def train_baseline(X_train, Y_train, alpha=1000):
    """Fit one Ridge model per target. Rows with a missing target are skipped."""
    scaler = StandardScaler().fit(X_train)
    X_scaled = scaler.transform(X_train)
    models = {}
    for target in Y_train.columns:
        not_missing = Y_train[target].notna().values
        model = Ridge(alpha=alpha)
        model.fit(X_scaled[not_missing], Y_train[target][not_missing])
        models[target] = model
    return scaler, models


def predict(scaler, models, X):
    """Predict all targets for the rows in X."""
    X_scaled = scaler.transform(X)
    preds = {}
    for target, model in models.items():
        preds[target] = model.predict(X_scaled)
    return pd.DataFrame(preds, index=X.index)
