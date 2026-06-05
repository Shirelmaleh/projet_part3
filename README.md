# Movie Rating Predictor

A Flask web application that predicts movie ratings using a trained Random Forest model.

## Team Members
- Liad Malachi: 212452882
- Shirel Elmaleh: 345653984

## Installation

1. Clone the repository:
   git clone https://github.com/Shirelmaleh/Machine-Learning.git
   cd projet_part3

2. Create a virtual environment:
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

## How to Run

python api.py

Then open your browser at: http://localhost:81

## Input Fields

| Field | Description | Example |
|---|---|---|
| Movie Title | Full title of the movie | Inception |
| Release Year | Year the movie was released (1895–2024) | 2010 |
| Duration | Runtime in minutes (60–300) | 148 |
| Genres | Comma-separated list of genres | Action,Sci-Fi,Thriller |
| Language | Primary language of the movie | English |

## Project Structure

| File | Description |
|---|---|
| api.py | Flask backend server |
| templates/index.html | Frontend HTML form |
| assets_data_prep.py | Data preparation function from Part 2 |
| model.pkl | Trained Random Forest model |
| requirements.txt | Required Python libraries |