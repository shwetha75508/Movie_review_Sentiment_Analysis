import streamlit as st
import joblib

# load model and vectorizer
model = joblib.load("movie_sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer(3).pkl")

# Page configuration
st.set_page_config(
    page_title = "Movie Review Sentiment Analysis",
    page_icon = "🎬",
    layout = "centered"
)

# App title
st.title("🎬 Movie Review Sentiment Analysis")

st.write("Analyze audience opinions and predict whether a movie review is "
    "**Positive** or **Negative**.")

# user input
review = st.text_area("Enter a movie review", height = 220)

# prediction
if st.button("Predict"):

    if not review.strip():
        st.warning("⚠ Please enter movie review.")

    else:
        # convert review into TF-IDF features
        vector = vectorizer.transform([review])

        # Prediction and Probabilities
        pred = model.predict(vector)[0]
        prob = model.predict_proba(vector)[0]

        positive_prob = prob[1] * 100
        negative_prob = prob[0] * 100

        # Display sentiment
        if pred == "positive":
            st.success("Sentiment: 😊Positive")
        else:
            st.error("Sentiment: 😞Negative")

        
        # Confidence Score
        confidence = max(positive_prob, negative_prob)
        st.subheader(f"Confidence Score: {confidence:.2f}%")

                    
    