import pandas as pd

DATA_DIR = "data/mitsui-commodity-prediction-challenge"


def load_data(data_dir=DATA_DIR):
    """Read the competition files and return them as DataFrames."""
    train = pd.read_csv(f"{data_dir}/train.csv")
    labels = pd.read_csv(f"{data_dir}/train_labels.csv")
    target_pairs = pd.read_csv(f"{data_dir}/target_pairs.csv")
    return train, labels, target_pairs
