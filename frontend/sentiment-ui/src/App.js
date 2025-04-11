import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [sentiment, setSentiment] = useState(null);
  const [error, setError] = useState(null);

  const handlePredict = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/predict', { text });
      setSentiment(response.data.sentiment);
      setError(null);
    } catch (err) {
      setError('Something went wrong. Try again.');
      setSentiment(null);
    }
  };

  return (
    <div className="container">
      <h1>Sentiment Analyzer</h1>
      <textarea
        rows="5"
        placeholder="Enter a review or comment..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={handlePredict}>Analyze Sentiment</button>

      {sentiment && (
        <div className={`result ${sentiment}`}>
          Sentiment: <strong>{sentiment.toUpperCase()}</strong>
        </div>
      )}

      {error && <div className="error">{error}</div>}
    </div>
  );
}

export default App;