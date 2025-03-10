# Plant 🌱 Disease 🐛 Detection 🔎

Plant Disease Detection is an advanced machine learning project that leverages Convolutional Neural Networks (CNN) and deep learning techniques to identify and classify plant diseases. Its primary goal is to provide farmers and agricultural experts with a reliable tool for rapid plant health diagnosis, enabling timely intervention and reducing the risk of crop loss.

[**Live Demo**](https://saurabhsinghdhami-plant-disease-detection-main-app-p8d5ks.streamlit.app/)

## Project Structure 📂
Key Features:
✅ Deep Learning-Based Detection – Uses CNN for high-accuracy plant disease classification.
✅ User-Friendly Interface – Upload leaf images and get instant predictions.
✅ Grad-CAM Visualization – Highlights affected areas in the leaf for better interpretability.
✅ Scalable & Customizable – Can be expanded to support more plant species and diseases.

## Installation 🚀

To run the project locally, follow these steps:

1. **Clone the repository:**

```bash
git clone https://github.com/SAURABHSINGHDHAMI/Plant-Disease-Detection.git
```

2. Navigate to the project directory:

```bash
cd Plant-Disease-Detection
```

3. **Install the required packages:**

```bash
pip install -r requirements.txt
```

4. **Run the Streamlit web application:**

```bash
streamlit run main_app.py
```

## Model Training 🧠

The model was trained using the `Plant_Disease_Detection.ipynb` notebook. It employs a Convolutional Neural Network architecture to classify plant images into different disease categories. The trained model weights are saved in `plant_disease_model.h5`.

## Web Application 🌐

The web application (`app.py`) empowers users to interact with the trained model. Upload plant images, and the application provides real-time predictions regarding the health of the plant.

## Requirements 🛠️

- Keras==2.8.0
- numpy==1.21.4
- streamlit==1.18.0
- opencv-python-headless==4.5.3
- tensorflow==2.7.0
