import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("best_movie_revenue_model.pkl")

# Page Config
st.set_page_config(page_title="🎬 Movie Revenue Predictor", page_icon="🎥", layout="centered")

# Banner
st.markdown("""
    <h1 style='text-align: center; color: #ff4b4b;'>🎬 Movie Revenue Predictor</h1>
    <p style='text-align: center; font-size: 18px;'>Estimate how much your movie could earn at the box office!</p>
    <hr style='border: 1px solid #f0f0f0;'>
""", unsafe_allow_html=True)

# Sidebar inputs
st.sidebar.header("📝 Movie Details")
budget = st.sidebar.number_input("💰 Budget (in millions)", min_value=0.0, value=50.0, step=1.0)
popularity = st.sidebar.slider("🔥 Popularity Score", 0.0, 100.0, 50.0)
runtime = st.sidebar.slider("🎞️ Runtime (minutes)", 30, 240, 120)
genre = st.sidebar.selectbox("🎭 Genre", ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Other"])
language = st.sidebar.selectbox("🌐 Language", ["en", "es", "fr", "de", "zh", "hi", "Other"])
vote_count = st.sidebar.number_input("🗳️ Vote Count", min_value=0, value=1000, step=100)
vote_avg = st.sidebar.slider("⭐ Average Vote", 0.0, 10.0, 7.0)

# Mapping categorical inputs
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

# Predict button
st.markdown("### 🎯 Ready to Predict?")
if st.button("🔮 Predict Box Office Revenue"):
    with st.spinner("Crunching numbers..."):
        features = np.array([[budget, popularity, runtime,
                              genre_mapping[genre], language_mapping[language],
                              vote_count, vote_avg]])
        prediction = model.predict(features)[0]
        formatted = f"${prediction:,.2f}"
        st.success("✅ Prediction Complete!")
        st.markdown(f"""
        <div style='background-color:#f0f2f6; padding: 30px 20px; border-radius: 10px; text-align: center; margin-top: 20px;'>
            <h2 style='color:#4CAF50;'>💵 Estimated Revenue:</h2>
            <h1 style='color:#2c3e50; font-size: 36px;'>{formatted}</h1>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr>
    <div style='text-align: center; color: grey; font-size: 14px;'>
        Made with ❤️ by your AI assistant
    </div>
""", unsafe_allow_html=True)
