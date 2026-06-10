from flask import Flask, request, jsonify, send_from_directory
import joblib
import pandas as pd
import numpy as np
import os
import threading
import requests
import time
 
app = Flask(__name__)
 
# Load the full pipeline
try:
    model = joblib.load('trained_model.pkl')
    print("Model loaded successfully")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")
 
 
def keep_alive():
    while True:
        time.sleep(600)
        try:
            requests.get('https://projet-part3-1.onrender.com')
        except:
            pass
 
threading.Thread(target=keep_alive, daemon=True).start()
 
 
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')
 
 
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
 
    try:
        data = request.get_json()
 
        required_fields = [
            'runtimeMinutes', 'movie_age', 'title_length', 'genre_count',
            'is_drama', 'is_documentary', 'is_comedy', 'is_action',
            'is_thriller', 'is_horror', 'is_romance', 'is_crime', 'is_english'
        ]
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400
 
        df_input = pd.DataFrame([{f: float(data[f]) for f in required_fields}])
 
        if hasattr(model, 'feature_names_in_'):
            df_input = df_input[model.feature_names_in_]
 
        prediction = model.predict(df_input)[0]
        return jsonify({'predicted_rating': round(float(prediction), 2)})
 
    except ValueError as e:
        return jsonify({'error': f'Invalid value: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Internal error: {str(e)}'}), 500
 
 
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)