import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the model from .h5 file
model = tf.keras.models.load_model('path/to/model.h5')

# Function to preprocess the image
def preprocess_image(image):
    # Resize the image to the required input shape of the model
    image = image.resize((224, 224))
    # Convert the image to numpy array
    image = np.array(image)
    # Normalize the image
    image = image / 255.0
    # Add an extra dimension to represent the batch size
    image = np.expand_dims(image, axis=0)
    return image

# Function to perform inference
def predict(image):
    # Preprocess the image
    image = preprocess_image(image)
    # Perform inference
    prediction = model.predict(image)
    # Get the predicted class label
    predicted_class = np.argmax(prediction)
    return predicted_class

# Streamlit app
def main():
    st.title("Image Inference")
    st.write("Upload an image and get the predicted class label")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image file
        image = Image.open(uploaded_file)
        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform inference
        predicted_class = predict(image)

        # Display the predicted class label
        st.write("Predicted Class:", predicted_class)

if __name__ == '__main__':
    main()