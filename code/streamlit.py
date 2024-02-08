import streamlit as st
import numpy as np
from PIL import Image
from keras.models import load_model

model = load_model("../data/model.h5")


# Function to preprocess the input image
def preprocess_image(image):
    img = image.convert("L").resize((28, 28))
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(-1, 28, 28, 1)
    return img_array


# Function to convert labels to letters
def map_label_to_letter(label):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters[label]


st.title("Sign Language Recognition App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    processed_image = preprocess_image(image)

    prediction = model.predict(processed_image)
    predicted_label = np.argmax(prediction)
    confidence_percentage = np.max(prediction) * 100

    predicted_letter = map_label_to_letter(predicted_label)

    st.write("Prediction:", predicted_letter)
    st.write("Confidence:", f"{confidence_percentage:.2f}%")
