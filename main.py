import streamlit as st
import pandas as pd
import numpy as np
import pickle 
from sklearn.ensemble import RandomForestClassifier
import joblib
import pickle

from PIL import Image

def main():
    # Define custom CSS styles
    custom_styles = """
        <style>
            /* Add your custom styles here */
            .custom-heading {
                color: #3498db; /* Custom font color (hex code) */
                font-size: 36px; /* Custom font size */
                font-weight: bold; /* Custom font weight */
                text-align: center; /* Custom text alignment */
                margin-bottom: 20px; /* Custom margin-bottom */
                text-decoration: underline; /* Custom text decoration */
            }
        </style>
    """

    # Display custom styles
    st.markdown(custom_styles, unsafe_allow_html=True)

    # Display heading with custom style
    st.markdown("<p class='custom-heading'> Prediciting Success of a Restaurant in Bangalore</p>", unsafe_allow_html=True)


    st.markdown("<p class='custom-heading'> TEXT ANALYSIS</p>", unsafe_allow_html=True)

    
    image1 = Image.open(r'ML_Restaurants_Success_Predictor-main\types.png')  
    st.image(image1, caption='varieties of restraunts', use_column_width=True)

    image2 = Image.open(r'ML_Restaurants_Success_Predictor-main\unique_features_line_plot.png')
    st.image(image2, caption='unique feeatures', use_column_width=True)

    image3 = Image.open(r'ML_Restaurants_Success_Predictor-main\cost2_stem.png')
    st.image(image3, caption='Average cost for 2 people ', use_column_width=True)
        
    image4 = Image.open(r'op\rating.png')
    st.image(image4, caption='Ratings', use_column_width=True)
        
    image5 = Image.open(r'ML_Restaurants_Success_Predictor-main\matrix.png')
    st.image(image5, caption='Confusion Matrix', use_column_width=True)

    st.markdown("<p class='custom-heading'> Result of Training </p>", unsafe_allow_html=True)

    image6 = Image.open(r'ML_Restaurants_Success_Predictor-main\comparision details.png')
    st.image(image6, caption='Results', use_column_width=True)


    if st.button("Next Page"):
        st.experimental_set_query_params(page="page2")

    st.markdown(
        """
        <style>
            div.stButton > button {
                position: fixed;
                bottom: 10px;
                right: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()




