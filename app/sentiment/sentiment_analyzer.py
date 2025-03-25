pip install transformers fer

# sentiment/sentiment_analyzer.py
from fer import FER
from transformers import pipeline

emotion_detector = FER(mtcnn=True)
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_facial_sentiment(frame):
    return emotion_detector.detect_emotions(frame)

def analyze_verbal_sentiment(text):
    return sentiment_pipeline(text)
