from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)  # Enable CORS so React can call the API

# Load the trained model
model_path = os.path.join('model', 'sentiment_model.pkl')
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    prediction = model.predict([text])[0]
    return jsonify({'sentiment': prediction})

if __name__ == '__main__':
    app.run(debug=True)
