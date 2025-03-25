# app/config.py

import os

# RTMP Stream Input
RTMP_URL = os.getenv("RTMP_URL", "rtmp://localhost/live/stream")

# Frame Capture
FRAME_OUTPUT_DIR = os.getenv("FRAME_OUTPUT", "/app/frames")

# YOLOv8 Model Config
YOLO_MODEL_PATH = os.getenv("YOLO_MODEL_PATH", "yolov8n.pt")
YOLO_CONFIDENCE_THRESHOLD = float(os.getenv("YOLO_CONFIDENCE", 0.3))

# Whisper / Transcription
WHISPER_MODEL_SIZE = os.getenv("WHISPER_MODEL", "large-v3")
AUDIO_INPUT_PATH = os.getenv("AUDIO_INPUT_PATH", "/app/audio_input")

# AWS S3
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME", "your-bucket")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "")

# MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "video_ai")

# General
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"
