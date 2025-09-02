import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, ConfusionMatrixDisplay

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
TRAIN_PATH = os.path.join(DATA_DIR, "train.csv")
TEST_PATH  = os.path.join(DATA_DIR, "test.csv")

def load_dataset(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Expected dataset at: {path}")
    df = pd.read_csv(path)
    return df

def split_features_labels(df: pd.DataFrame):
    if "fake" not in df.columns:
        raise KeyError("The dataset must contain a 'fake' target column (1 = fake, 0 = genuine).")
    X = df.drop(columns=["fake"])
    y = df["fake"].astype(int)
    return X, y

def train_and_evaluate(X_train, X_val, y_train, y_val) -> RandomForestClassifier:
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=42,
        n_jobs=-1,
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    print("\n=== Validation Report ===")
    print(classification_report(y_val, y_pred, digits=3))

    # Confusion Matrix
    disp = ConfusionMatrixDisplay.from_predictions(y_val, y_pred, display_labels=["Genuine", "Fake"])
    plt.title("Confusion Matrix (Validation)")
    plt.tight_layout()
    plt.show()

    # Feature importance
    importances = model.feature_importances_
    order = np.argsort(importances)[::-1]
    plt.figure(figsize=(8, max(4, len(order)*0.3)))
    plt.barh(np.array(X_train.columns)[order][::-1], importances[order][::-1])
    plt.xlabel("Importance")
    plt.title("Feature Importances (RandomForest)")
    plt.tight_layout()
    plt.show()

    return model

def main():
    print("Loading datasets...")
    df_train = load_dataset(TRAIN_PATH)
    print(f"Train shape: {df_train.shape}")
    print(df_train.head(3))

    # Check schema quickly
    expected = [
        'profile pic', 'nums/length username', 'fullname words', 'nums/length fullname',
        'name==username', 'description length', 'external URL', 'private',
        '#posts', '#followers', '#follows', 'fake'
    ]
    missing = [c for c in expected if c not in df_train.columns]
    if missing:
        print("WARNING: These expected columns were not found:", missing)
        print("Proceeding with whatever columns exist, as long as 'fake' is present.")

    X, y = split_features_labels(df_train)

    # Basic split (we already have a provided test.csv, so here we do a small validation set)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    model = train_and_evaluate(X_train, X_val, y_train, y_val)

    # Optional: Evaluate on provided test split (if available)
    if os.path.exists(TEST_PATH):
        print("\nLoading held-out test set...")
        df_test = load_dataset(TEST_PATH)
        if 'fake' in df_test.columns:
            X_test, y_test = split_features_labels(df_test)
            test_pred = model.predict(X_test)
            print("\n=== Test Report (held-out) ===")
            print(classification_report(y_test, test_pred, digits=3))
            disp = ConfusionMatrixDisplay.from_predictions(y_test, test_pred, display_labels=["Genuine", "Fake"])
            plt.title("Confusion Matrix (Test)")
            plt.tight_layout()
            plt.show()
        else:
            print("Note: test.csv does not contain 'fake' labels; skipping final report.")
    else:
        print("No test.csv found. Skipping held-out test evaluation.")

if __name__ == '__main__':
    main()
