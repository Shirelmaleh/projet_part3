# Movie Rating Predictor
 
A Flask web application that predicts movie ratings using a trained Random Forest model.
 
## Team Members
- Liad Malachi: 212452882
- Shirel Elmaleh: 345653984
## Project Description
This application is part 3 of the final assignment for the Machine Learning course.
It wraps the trained Random Forest model from part 2 into a Flask web service that allows
users to directly input the model features and receive a predicted IMDb rating in real time.
 
## System Architecture
Browser (HTML Form) → JSON Request → Flask API → Random Forest → Predicted Rating → Browser
 
## Installation
 
1. Clone the repository:
   git clone https://github.com/Shirelmaleh/projet_part3.git
   cd projet_part3
2. Create a virtual environment:
   python -m venv venv
   venv\Scripts\activate
3. Install dependencies:
   pip install -r requirements.txt
## How to Run (Local)
 
python api.py
 
Then open your browser at: http://localhost:5000
 
## Live Demo
 
https://projet-part3-3.onrender.com
 
## Input Fields
 
| Field | Description | Expected Values |
|---|---|---|
| runtimeMinutes | Runtime of the movie in minutes | 60 – 300 |
| movie_age | Number of years since release (2026 - release year) | e.g. 16 |
| title_length | Number of characters in the movie title | e.g. 9 |
| genre_count | Number of genres associated with the movie | e.g. 3 |
| is_drama | Whether the movie is a Drama | 0 or 1 |
| is_documentary | Whether the movie is a Documentary | 0 or 1 |
| is_comedy | Whether the movie is a Comedy | 0 or 1 |
| is_action | Whether the movie is an Action film | 0 or 1 |
| is_thriller | Whether the movie is a Thriller | 0 or 1 |
| is_horror | Whether the movie is a Horror film | 0 or 1 |
| is_romance | Whether the movie is a Romance | 0 or 1 |
| is_crime | Whether the movie is a Crime film | 0 or 1 |
| is_english | Whether the movie is in English | 0 or 1 |
 
## Project Structure
 
| File | Description |
|---|---|
| api.py | Flask backend server with /predict endpoint |
| index.html | Frontend HTML form with fetch API |
| trained_model.pkl | Trained Random Forest pipeline (joblib) |
| requirements.txt | Required Python libraries |
| README.md | Project documentation |
 
## API Endpoints
 
| Endpoint | Method | Description |
|---|---|---|
| / | GET | Returns the HTML form |
| /predict | POST | Accepts JSON with the 13 features, returns predicted_rating |
 
## Technical Notes
- The full pipeline (preprocessor + model) is saved in trained_model.pkl using joblib with maximum compression to stay under 25MB
- The HTML form now exposes the 13 model features directly — no server-side feature engineering needed
- Error handling returns status 400 for missing or invalid fields, 500 for internal errors
 