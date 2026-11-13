# GROUP57_CENG313

CENG313 Introduction to Data Science course project.

## Group

| Group ID | Member | Student ID |
|---|---|---|
| 57 | Berke Vural | 23118080755 |

## Competition

[MITSUI&CO. Commodity Prediction Challenge](https://www.kaggle.com/competitions/mitsui-commodity-prediction-challenge)

The goal is to predict 424 future returns of commodity related instruments from daily
prices of LME, JPX, US stocks and Forex.

## Data

The data is not in this repository, because of the Kaggle rules and the file size.
Join the competition on Kaggle, accept the rules and download all files from the
Data tab. Unzip them so that the files are in
`data/mitsui-commodity-prediction-challenge/`, for example
`data/mitsui-commodity-prediction-challenge/train.csv`.

## How to run

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/jupyter notebook
```

Start Jupyter from the repository folder, so that `from src.data import ...` works.
Then open `assignment1_eda_baseline.ipynb` and run all cells.

`kaggle_submission.ipynb` is meant to run on Kaggle. It needs the competition data and
our `src` files (uploaded as a Kaggle dataset) as inputs.

## Repository structure

```
assignment1_eda_baseline.ipynb   Assignment 1, EDA and baseline
kaggle_submission.ipynb          late submission notebook for Kaggle
src/data.py                      loading and preprocessing
src/models.py                    Ridge baseline (train and predict)
src/utils.py                     competition metric
submissions/                     submission screenshot
```

## Score

**Competition closed — evaluated on a held-out split.**

Kaggle does not accept submissions for this competition any more (screenshot in
`submissions/`). We report the score on the last 20 % of the training days, computed
with the competition metric.

| Model | Held-out score |
|---|---|
| Mean of each target (no features) | 0.216 |
| Ridge regression, alpha = 100000 (our baseline) | 0.197 |
| Best team on the final leaderboard | 0.638 |
