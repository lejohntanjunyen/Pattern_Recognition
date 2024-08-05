import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# To run this file, use the following: streamlit run main.py
# I suggest entering src and running it from there, so the path to the model is correct.

# Load the model from keras file
try:
    model = tf.keras.models.load_model('/Users/lejohntanjunyen/Documents/Pattern_Recognition/Pattern_Recognition/src/resnet.keras', compile=True )
    st.write("Model loaded successfully.")
except Exception as e:
    st.write("Error loading model:", e)


unique_classes = np.load('/Users/lejohntanjunyen/Documents/Pattern_Recognition/Pattern_Recognition/src/class_order.npy')

class_index_to_label = {index: label for index, label in enumerate(unique_classes)}

# Function to preprocess the image
def preprocess_image(image):
    try:
        # Resize the image to the required input shape of the model
        image = image.resize((224, 224))
        # Convert the image to numpy array
        image = np.array(image)
        # Normalize the image
        # image = image / 255.0
        # Add an extra dimension to represent the batch size
        image = np.expand_dims(image, axis=0)
        return image
    except Exception as e:
        st.write("Error in preprocessing image:", e)
        return None

# Function to perform inference
def predict(image):
    try:
        # Preprocess the image
        image = preprocess_image(image)
        if image is not None:
            # Perform inference
            prediction = model.predict(image)
            predicted_probabilities = prediction[0]

            # Get the predicted class index
            predicted_class_index = np.argmax(predicted_probabilities)
            st.write("Predicted class index:", predicted_class_index)

            # Map the class index to the class label
            predicted_class_label = unique_classes[predicted_class_index]

            return predicted_class_label
        else:
            return None
    except Exception as e:
        st.write("Error in prediction:", e)
        return None


# Streamlit app
def main():
    st.title("Logo Inference")
    st.write("Upload an image to perform inference and predict the logo class.")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg"])

    if uploaded_file is not None:
        try:
            # Read the image file
            image = Image.open(uploaded_file)
            # Display the uploaded image
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Perform inference
            predicted_class = predict(image)

            if predicted_class is not None:
                # Display the predicted class label
                st.write("Predicted Class:", predicted_class)
            else:
                st.write("Prediction failed.")
        except Exception as e:
            st.write("Error processing the uploaded file:", e)

if __name__ == '__main__':
    main()


