from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the full pipeline
try:
    model = joblib.load('model.pkl')
    print("Model loaded successfully")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")


def prepare_input(data):
    """Recreate the features from raw input, matching prepare_data() from part 2."""
    runtime = float(data['runtimeMinutes'])
    start_year = int(data['startYear'])
    title = str(data['primaryTitle'])
    genres = str(data['genres']).lower()
    language = str(data['language']).lower()

    row = {
        'runtimeMinutes': runtime if 60 <= runtime <= 300 else np.nan,
        'movie_age': 2026 - start_year if 1895 <= start_year <= 2024 else np.nan,
        'title_length': len(title),
        'genre_count': len(genres.split(',')) if genres not in ['\\n', 'nan'] else 0,
        'is_drama':        1 if 'drama'       in genres else 0,
        'is_documentary':  1 if 'documentary' in genres else 0,
        'is_comedy':       1 if 'comedy'       in genres else 0,
        'is_action':       1 if 'action'       in genres else 0,
        'is_thriller':     1 if 'thriller'     in genres else 0,
        'is_horror':       1 if 'horror'       in genres else 0,
        'is_romance':      1 if 'romance'      in genres else 0,
        'is_crime':        1 if 'crime'        in genres else 0,
        'is_english':      1 if 'english'      in language else 0,
    }

    df = pd.DataFrame([row])
    if hasattr(model, 'feature_names_in_'):
        df = df[model.feature_names_in_]
    return df


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500

    try:
        data = request.get_json()

        required_fields = ['runtimeMinutes', 'startYear', 'primaryTitle', 'genres', 'language']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        df_input = prepare_input(data)
        prediction = model.predict(df_input)[0]

        return jsonify({'predicted_rating': round(float(prediction), 2)})

    except ValueError as e:
        return jsonify({'error': f'Invalid value: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Internal error: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
