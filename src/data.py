import pandas as pd

DATA_DIR = "data/mitsui-commodity-prediction-challenge"


def load_data(data_dir=DATA_DIR):
    """Read the competition files and return them as DataFrames."""
    train = pd.read_csv(f"{data_dir}/train.csv")
    labels = pd.read_csv(f"{data_dir}/train_labels.csv")
    target_pairs = pd.read_csv(f"{data_dir}/target_pairs.csv")
    return train, labels, target_pairs


def preprocess(train):
    """Turn the raw prices into daily log returns."""
    close_cols = [col for col in train.columns
                  if col.startswith("FX")
                  or col.endswith("_Close")
                  or col.endswith("_adj_close")]
    prices = train[close_cols]
    prices = prices.drop(columns=["US_Stock_GOLD_adj_close"])
    prices = prices.ffill()
    return prices
