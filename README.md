# 🎬 Movie Review Sentiment Analysis
The goal of this project is to analyze audience opinions from movie reviews and predict whether the sentiment is positive or negative.

## 📌 Project Overview
With the growing number of movie reviews available online, manually analyzing audience opinions can be time-consuming. This project uses Natural Language Processing (NLP) and Machine Learning to automatically classify movie reviews based on their sentiment.

---
## 📂 Dataset

- **Dataset:** IMDb Movie Reviews Dataset
- **Records:** 49,582
- **Features:** 2
- **Text Column:** review
- **Target Variable:** sentiment(Positive, Negative)

---
## 🛠 Technologies Used

- Python
- NLP
- TF-IDF Vectorizer
- Scikit-learn
- Streamlit
- Joblib

---
## 🤖 Machine Learning Models

- Multinomial Naive Bayes ✅ 
- Decision Tree
- K-Nearest Neighbors (KNN)

The Multinomial Naive Bayes achieved the best performance and was selected as the final model for deployement.


--- 
## 📁 Project Structure

```
Movie_Review_Sentiment/
│
├── app.py
├── movie_sentiment_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md
└── dataset.csv

---
## ▶️ Run the Project
1. Install the required libraries:

```bash
pip install -r requirements.txt
```

2. Run the Streamlit application:

```bash
streamlit run app.py
```

## 👩‍💻 Developer
Shweta Rani

- LinkedIn: https://www.linkedin.com/in/shweta-rani-13598636a/
- HuggingFace: https://huggingface.co/spaces/shweta117/credit_risk_proj1

--- 

