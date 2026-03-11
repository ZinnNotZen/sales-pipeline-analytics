import pandas as pd


def total_pipeline_value(pipeline):
    return pipeline["close_value"].sum()


def win_rate(pipeline):

    closed_deals = pipeline[pipeline["is_closed"]]

    wins = closed_deals[closed_deals["is_won"]].shape[0]
    total = closed_deals.shape[0]

    return wins / total


def average_deal_size(pipeline):

    won_deals = pipeline[pipeline["is_won"]]

    return won_deals["close_value"].mean()


def deals_by_stage(pipeline):

    return pipeline["deal_stage"].value_counts()


def revenue_by_rep(pipeline):

    return pipeline.groupby("sales_agent")["close_value"].sum().sort_values(ascending=False)