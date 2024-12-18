import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

def load_incident_detection_model(model_path):
    return load_model(model_path)

def detect_incident(frame, model):
    frame_processed = preprocess_frame(frame)
    prediction = model.predict(frame_processed)
    return np.argmax(prediction, axis=1)

def preprocess_frame(frame):
    frame_resized = cv2.resize(frame, (224, 224))
    frame_normalized = frame_resized / 255.0
    return frame_normalized.reshape((1, 224, 224, 3))
