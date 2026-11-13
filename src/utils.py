import pandas as pd


def daily_spearman(y_true, y_pred):
    """Spearman correlation between true and predicted targets for each day."""
    corrs = []
    for i in range(len(y_true)):
        true_row = y_true.iloc[i]
        pred_row = y_pred.iloc[i]
        not_missing = true_row.notna()
        corr = true_row[not_missing].corr(pred_row[not_missing], method="spearman")
        corrs.append(corr)
    return pd.Series(corrs)


def sharpe_score(y_true, y_pred):
    """Competition metric: mean of the daily correlations divided by their std."""
    corrs = daily_spearman(y_true, y_pred)
    return corrs.mean() / corrs.std(ddof=0)
