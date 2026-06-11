import os
import pickle
import pandas as pd

from preprocess import clean_text

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

os.makedirs("models", exist_ok=True)

print("Loading dataset...")

df = pd.read_csv(
    "data/spam.csv",
    sep="\t"
)

print("Dataset Loaded Successfully")

df.columns = [
    "label",
    "message"
]

df["message"] = df["message"].apply(
    clean_text
)

X = df["message"]
y = df["label"]

vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Model...")

model = LinearSVC(
    random_state=42
)

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    predictions
)

precision = precision_score(
    y_test,
    predictions,
    pos_label="spam"
)

recall = recall_score(
    y_test,
    predictions,
    pos_label="spam"
)

f1 = f1_score(
    y_test,
    predictions,
    pos_label="spam"
)

print("\nResults")
print("-------------------")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")

with open(
    "models/phishing_model.pkl",
    "wb"
) as f:
    pickle.dump(
        model,
        f
    )

with open(
    "models/vectorizer.pkl",
    "wb"
) as f:
    pickle.dump(
        vectorizer,
        f
    )

print("\nModel Saved Successfully")