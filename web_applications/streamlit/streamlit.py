import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
from keras.preprocessing import image

st.markdown("<h1 align='center'>ASL Alphabet Interpreter</h1>", unsafe_allow_html=True)
st.markdown("<h5 align='center'>This model interprets American Sign Language (ASL) alphabet images.</h5>", unsafe_allow_html=True)

file = st.file_uploader("Upload your image:", type=["jpeg", "jpg", "png"])

if file is not None:
    images = Image.open(file).convert("RGB")
    st.image(images, use_column_width=True)

    model = load_model("../../data/model.keras")

    img = images.resize((256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    class_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
    predicted_class = class_labels[np.argmax(prediction)]
    
    st.markdown(f"<h3 align='center'>Prediction: {predicted_class}</h3>", unsafe_allow_html=True)