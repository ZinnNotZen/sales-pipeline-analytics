import pandas as pd


def load_data(data_path="../data/"):
    
    accounts = pd.read_csv(f"../data/accounts.csv")
    products = pd.read_csv(f"../data/products.csv")
    sales_teams = pd.read_csv(f"../data/sales_teams.csv")
    pipeline = pd.read_csv(f"../data/sales_pipeline.csv")

    return accounts, products, sales_teams, pipeline


def clean_pipeline(pipeline):

    pipeline["engage_date"] = pd.to_datetime(pipeline["engage_date"])
    pipeline["close_date"] = pd.to_datetime(pipeline["close_date"])

    pipeline = pipeline.dropna(subset=["engage_date"])

    pipeline["account"] = pipeline["account"].fillna("Unknown")

    pipeline["is_closed"] = pipeline["deal_stage"].isin(["Won", "Lost"])
    pipeline["is_won"] = pipeline["deal_stage"] == "Won"

    pipeline["sales_cycle_days"] = (
        pipeline["close_date"] - pipeline["engage_date"]
    ).dt.days

    return pipeline