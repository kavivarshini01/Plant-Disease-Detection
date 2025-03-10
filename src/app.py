# Import necessary libraries
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
# Import the preprocessing function
from preprocessing import preprocess_image

# Load the trained model
MODEL_PATH = "../models/plant_disease_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Class labels
CLASS_NAMES = ['Healthy', 'Mild Disease', 'Moderate Disease', 'Severe Disease']

# Streamlit App
st.title("🌿 Plant Disease Detection System")
st.markdown("Upload an image of a plant leaf to detect possible diseases.")

# File uploader
uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Use preprocessing function
    img_array = preprocess_image(image)  # ✅ Now using the function from preprocessing.py
    
    # Debugging: Print the shape of img_array before prediction
    st.write(f"Image shape before prediction: {img_array.shape}")
    
    # Make prediction
    predictions = model.predict(img_array)
    st.write(f"Raw model output: {predictions}")  # Debugging: Print raw output from model
    
    predicted_class = np.argmax(predictions)
    confidence = np.max(predictions) * 100
    
    # Display results
    st.subheader("Prediction Result")
    st.success(f"Predicted Disease: {CLASS_NAMES[predicted_class]}")
    st.info(f"Confidence Level: {confidence:.2f}%")
    
    st.markdown("---")
    st.markdown("### ℹ About This Model")
    st.write(
        "This model detects plant diseases using a convolutional neural network (CNN). The dataset includes images categorized as Healthy, Mild, Moderate, and Severe disease levels."
    )
    
    st.markdown("---")
    st.markdown("#### 🔗 Source & Attribution")
    st.write("This project was modified based on an open-source implementation. Original work credited to the respective authors.")
