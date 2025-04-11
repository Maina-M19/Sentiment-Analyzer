# Sentiment Analyzer for Product Reviews

A full-stack web application that analyzes the sentiment of user-submitted reviews or comments (e.g., from Amazon or Twitter) and classifies them as **Positive**, **Neutral**, or **Negative**. Built using Python (Flask) for the backend and React for the frontend.

---

## Features

- Train and save a logistic regression model using scikit-learn
- REST API built with Flask to serve real-time predictions
- React frontend for user input and displaying sentiment results
- CORS-enabled communication between frontend and backend

---

## Tech Stack

- **Frontend**: React, Axios
- **Backend**: Python, Flask, scikit-learn, joblib, Flask-CORS
- **Model**: Logistic Regression with TF-IDF vectorizer
- **Tools**: Postman (for API testing), VS Code (for dev)

---

## Project Structure

```
sentiment-analyzer/
├── backend/
│   ├── app.py                  # Flask app with /predict API
│   ├── model/
│   │   ├── train_model.py      # Model training script
│   │   ├── sentiment_model.pkl # Saved ML model
│   │   └── sentiment_data.csv  # CSV with labeled text data
│   └── requirements.txt        # Python dependencies
├── frontend/
│   └── sentiment-ui/           # React app
└── README.md
```

---

## Setup Instructions

### 1. Backend (Flask API)

```bash
cd backend
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cd model
python train_model.py         # Trains and saves model
cd ..
python app.py                 # Starts Flask server at http://127.0.0.1:5000
```

### 2. Frontend (React App)

```bash
cd frontend
npx create-react-app sentiment-ui
cd sentiment-ui
npm install axios
npm start                     # Starts frontend at http://localhost:3000
```

---

## Example Usage

1. Open the app at `http://localhost:3000`
2. Enter a review like:  
   `"This is the best product I’ve ever used!"`
3. Click "Analyze Sentiment"
4. Output:  
   `Sentiment: POSITIVE`

---

## Future Enhancements

- Upgrade to Hugging Face Transformers (DistilBERT) for better accuracy
- Add charts for sentiment analysis stats
- Enable batch predictions
- Dockerize and deploy to Render or Railway
- Add CI/CD with GitHub Actions

---

## License

This project is open-source and free to use under the MIT license.

