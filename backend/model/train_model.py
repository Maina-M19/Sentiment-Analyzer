import pandas as pd
import joblib
import re
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report

# -------------------------------
# 1. Preprocessing Function
# -------------------------------
def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# -------------------------------
# 2. Load Dataset from CSV
# -------------------------------
try:
    df = pd.read_csv("sentiment_data.csv")
except FileNotFoundError:
    raise FileNotFoundError("❌ CSV file not found. Please make sure 'sentiment_data.csv' exists in the same directory.")

# -------------------------------
# 3. Clean and Preprocess Text
# -------------------------------
df.dropna(subset=["text", "label"], inplace=True)
df["text"] = df["text"].astype(str).apply(preprocess)

# -------------------------------
# 4. Train/Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

# -------------------------------
# 5. Build TF-IDF + Logistic Regression pipeline
# -------------------------------
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1, 2))),
    ('clf', LogisticRegression(max_iter=1000))
])

# -------------------------------
# 6. Train Model
# -------------------------------
pipeline.fit(X_train, y_train)

# -------------------------------
# 7. Evaluate Model
# -------------------------------
print("\n📊 Evaluation Report:\n")
print(classification_report(y_test, pipeline.predict(X_test)))

# -------------------------------
# 8. Save Model
# -------------------------------
joblib.dump(pipeline, "sentiment_model.pkl")
print("\n✅ Model trained and saved as 'sentiment_model.pkl'")
