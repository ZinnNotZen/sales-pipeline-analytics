from data_cleaning import load_data, clean_pipeline
from pipeline_metrics import win_rate


def main():

    accounts, products, sales_teams, pipeline = load_data()

    pipeline = clean_pipeline(pipeline)

    print("Win Rate:", win_rate(pipeline))


if __name__ == "__main__":
    main()