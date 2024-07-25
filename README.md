# Pattern_Recognition
## Logo Detection
## 27 Brands (Logos)
## Python Development (Could convert to MATLAB)
## Info Pack
 - Inspiration on Assignment: https://github.com/tadowney/logo_detection/tree/main/data
 - Kaggle Dataset Used: https://www.kaggle.com/code/sushovansaha9/xception-flickr27-brand-logo-detection
 - Team's Word Document for Documentation: https://cloudmails-my.sharepoint.com/:w:/r/personal/tp068254_mail_apu_edu_my/_layouts/15/doc2.aspx?sourcedoc=%7B8ABD00AA-FEAA-48A0-B20E-40F42A338061%7D&file=PR%20assignment.docx&action=default&mobileredirect=true&DefaultItemOpen=1&web=1
   
## DATA HERE: 
 - https://www.kaggle.com/datasets/sushovansaha9/flickr-logos-27-dataset/data

# Coding Process Flow
1. Extract and Load Data (Flickr32 Images, Flickr32 Labels, Flickr32 BBox)
2. Map Data and Label (Flickr32 Images, Flickr32 Labels, Flickr32 BBox)
3. PreProcessing (Cropping Image, Image Augmentation)
4. Feature Extraction ([Might not be needed])
5. Split Train and Test Data (Train Test Validation Split)
6. Training Model (CNN, ResNet50) [ResNet50 could be under Optimization] 
7. Validation (Validation Images Accuracy)
8. Testing (Test Images Accuracy)
9. Optimization (Hyper Parameter Tuning, [TBD])
10. Deployment and Integration (Gradio / StreamLit) [Web-interface for users to upload images to use the pattern recognition model]

# Things to Do (Documentation)
1. Literature Review
- a. Abstract
- b. Introduction
- c. Research Objectives
- d. Related Literature Reviews
2. Model Implementation and validation
- a. Methods
- b. Dataset Preparation
  - Cropping
  - Preprocessing
    - Padding
    - Resize Image
    - Normalise Image
    - Convert to array
    - Label Encoder
  - Split Train Test Images
    - Augment training images
- c. Model implementation
    - CNN Model
    - CNN Model + BiLSTM
    - ResNet Model
- e. Analysis and Recommendations
3. References


## Roles 
1. William
     - CNN Modelling
     - CNN Modelling + BiLSTM
   
3. Maadh (Away in August)
     - ResNet Modelling
     - Streamlit GUI Deployment and Integration
   
5. Jun-Yen
     - Extraction
     - PreProcessing
     - Splitting Data
     - Image Augmentation
   
