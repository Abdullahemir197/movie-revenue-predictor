from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize app
app = FastAPI(title="Movie Revenue Predictor API")

# Load model
model = joblib.load("best_movie_revenue_model.pkl")

# Mappings
genre_mapping = {
    "Action": 0,
    "Comedy": 1,
    "Drama": 2,
    "Horror": 3,
    "Romance": 4,
    "Sci-Fi": 5,
    "Other": 6
}
language_mapping = {
    "en": 0,
    "es": 1,
    "fr": 2,
    "de": 3,
    "zh": 4,
    "hi": 5,
    "Other": 6
}

# Request schema
class MovieData(BaseModel):
    budget: float
    popularity: float
    runtime: int
    genre: str
    language: str
    vote_count: int
    vote_avg: float

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Revenue Predictor API!"}

# Prediction endpoint
@app.post("/predict")
def predict(data: MovieData):
    try:
        features = np.array([[data.budget,
                              data.popularity,
                              data.runtime,
                              genre_mapping.get(data.genre, 6),
                              language_mapping.get(data.language, 6),
                              data.vote_count,
                              data.vote_avg]])
        prediction = model.predict(features)[0]
        return {"predicted_revenue": round(prediction, 2)}
    except Exception as e:
        return {"error": str(e)}
