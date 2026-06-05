# Movie Rating Predictor

A Flask web application that predicts movie ratings using a trained Random Forest model.

## Team Members
- Liad Malachi: 212452882
- Shirel Elmaleh: 345653984

## Project Description
This application is part 3 of the final assignment for the Machine Learning course.
It wraps the trained Random Forest model from part 2 into a Flask web service that allows
users to input movie parameters and receive a predicted IMDb rating in real time.

## System Architecture
Browser (HTML Form) → JSON Request → Flask API → prepare_data() → Random Forest → Predicted Rating → Browser

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
| Movie Title | Full title of the movie | Any text (e.g. Inception) |
| Release Year | Year the movie was released | 1895 – 2024 |
| Duration | Runtime in minutes | 60 – 300 |
| Genres | Comma-separated list of genres | e.g. Action,Sci-Fi,Thriller |
| Language | Primary language of the movie | e.g. English |

## Project Structure

| File | Description |
|---|---|
| api.py | Flask backend server with /predict endpoint |
| templates/index.html | Frontend HTML form with fetch API |
| assets_data_prep.py | prepare_data() function copied from part 2 |
| model.pkl | Trained Random Forest pipeline (joblib) |
| requirements.txt | Required Python libraries |
| README.md | Project documentation |

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| / | GET | Returns the HTML form |
| /predict | POST | Accepts JSON, returns predicted_rating |

## Technical Notes
- The full pipeline (preprocessor + model) is saved in model.pkl using joblib with maximum compression to stay under 25MB
- Features are reconstructed in api.py to match exactly what prepare_data() produces
- Error handling returns status 400 for missing or invalid fields, 500 for internal errors