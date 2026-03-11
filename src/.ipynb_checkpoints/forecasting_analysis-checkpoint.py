import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


def prepare_features(pipeline, accounts):

    data = pipeline.merge(accounts, on="account", how="left")

    data = data.dropna(subset=["close_value"])

    features = data[[
        "product",
        "sector",
        "employees"
    ]]

    features = pd.get_dummies(features)

    target = data["is_won"]

    return features, target


def train_model(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print(classification_report(y_test, predictions))

    return model