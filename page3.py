import streamlit as st
import pandas as pd
import numpy as np
import pickle 
from sklearn.ensemble import RandomForestClassifier
import joblib
import pickle

def page3():
    st.title("Page 3")

    with open('logreg.pkl', 'rb') as model_file:
        loaded_model = pickle.load(model_file)


    st.title("Prediciting Success of a Restaurant in Bangalore City using logistic regression")

    st.title("Training Accuracy App")

    # # Display the training accuracy
    # st.write(f"Training Accuracy: {train_accuracy:.2%}")

    multipleTypes = {'multiple_types': 1}
    totalCuisines = {'total_cuisines': 0}
    approxCost = {'approx_cost(for two people)': 1500}
    onlineOrder = {'online_order_Yes': 1}
    bookTable = {'book_table_Yes': 1}
    location = {'location_BTM': 0, 'location_Banashankari': 0, 'location_Banaswadi': 0,'location_Bannerghatta Road': 0,
    'location_Basavanagudi': 0,'location_Bellandur': 0,'location_Brigade Road': 0,
    'location_Brookefield': 0,'location_Church Street': 0,'location_Commercial Street': 0,
    'location_Cunningham Road': 0,'location_Domlur': 0,'location_Ejipura': 0,'location_Electronic City': 0,
    'location_Frazer Town': 0,'location_HSR': 0,'location_Indiranagar': 0,'location_JP Nagar': 0,
    'location_Jayanagar': 0,'location_Jeevan Bhima Nagar': 0,'location_Kalyan Nagar': 0,
    'location_Kammanahalli': 0,'location_Koramangala 1st Block': 0,'location_Koramangala 3rd Block': 0,
    'location_Koramangala 4th Block': 0,'location_Koramangala 5th Block': 0,'location_Koramangala 6th Block': 0,
    'location_Koramangala 7th Block': 0,'location_Koramangala 8th Block': 0,
    'location_Lavelle Road': 0,'location_MG Road': 0,'location_Malleshwaram': 0,
    'location_Marathahalli': 0,'location_New BEL Road': 0,'location_Old Airport Road': 0,
    'location_Rajajinagar': 0,'location_Residency Road': 0,'location_Richmond Road': 0,
    'location_Sarjapur Road': 0,'location_Shanti Nagar': 0,'location_Shivajinagar': 0,
    'location_St. Marks Road': 0,'location_Ulsoor': 0,'location_Vasanth Nagar': 0,
    'location_Whitefield': 0,'location_Wilson Garden': 0,'location_other': 0}


    st.write('Does your restaurant serves more than 1 type of Dish?')
    optionMultitype = st.selectbox(
        'Pick Yes or No.',
        ('Yes', 'No'))

    if optionMultitype == "Yes":
        multipleTypes['multiple_types'] = 2

    st.write("Select total number of Cuisines for your Restaurant")
    totalCuisinesNumber = st.selectbox(
        'Pick One Number',
        [1,2,3,4,5,6,7,8])
    totalCuisines['total_cuisines'] = totalCuisinesNumber

    st.write("Enter the Approx Cost for Two People")
    costForTwo = st.number_input('Insert a number', min_value = 40.0, max_value = 6000.0, value = 500.0, step = 0.1)
    approxCost['approx_cost(for two people)'] = float(costForTwo)

    st.write("Select the Location For your Restaurant")
    locationForRest = st.selectbox('Pick One Location',['location_BTM','location_Banashankari','location_Banaswadi',
    'location_Bannerghatta Road','location_Basavanagudi','location_Bellandur',
    'location_Brigade Road','location_Brookefield','location_Church Street',
    'location_Commercial Street','location_Cunningham Road','location_Domlur',
    'location_Ejipura','location_Electronic City','location_Frazer Town',
    'location_HSR','location_Indiranagar','location_JP Nagar',
    'location_Jayanagar','location_Jeevan Bhima Nagar','location_Kalyan Nagar',
    'location_Kammanahalli','location_Koramangala 1st Block','location_Koramangala 3rd Block',
    'location_Koramangala 4th Block','location_Koramangala 5th Block','location_Koramangala 6th Block',
    'location_Koramangala 7th Block','location_Koramangala 8th Block','location_Lavelle Road',
    'location_MG Road','location_Malleshwaram','location_Marathahalli',
    'location_New BEL Road','location_Old Airport Road','location_Rajajinagar',
    'location_Residency Road','location_Richmond Road','location_Sarjapur Road',
    'location_Shanti Nagar','location_Shivajinagar','location_St. Marks Road',
    'location_Ulsoor','location_Vasanth Nagar','location_Whitefield',
    'location_Wilson Garden','location_other'])

    location[locationForRest]=1

    restType = {'rest_type_Bakery': 0,'rest_type_Bar': 0,'rest_type_Beverage Shop': 0,
    'rest_type_Cafe': 0,'rest_type_Casual Dining': 0,'rest_type_Casual Dining, Bar': 0,
    'rest_type_Delivery': 0,'rest_type_Dessert Parlor': 0,'rest_type_Quick Bites': 0,
    'rest_type_Takeaway, Delivery': 0,'rest_type_other': 0}

    st.write("Select the Type of Restaurant")
    typeOfRest = st.selectbox(
        'Pick One',
        ['rest_type_Bakery','rest_type_Bar','rest_type_Beverage Shop',
    'rest_type_Cafe','rest_type_Casual Dining','rest_type_Casual Dining, Bar',
    'rest_type_Delivery','rest_type_Dessert Parlor','rest_type_Quick Bites',
    'rest_type_Takeaway, Delivery','rest_type_other'])
    restType[typeOfRest] = 1

    listedIn = {'listed_in(type)_Buffet': 0,'listed_in(type)_Cafes': 0,'listed_in(type)_Delivery': 0,
    'listed_in(type)_Desserts': 0,'listed_in(type)_Dine-out': 0,
    'listed_in(type)_Drinks & nightlife': 0,'listed_in(type)_Pubs and bars': 0}

    st.write("Select the type you are Listed In")
    typeOfListedIn = st.selectbox("Select One of the following", ['listed_in(type)_Buffet',
    'listed_in(type)_Cafes','listed_in(type)_Delivery','listed_in(type)_Desserts',
    'listed_in(type)_Dine-out','listed_in(type)_Drinks & nightlife','listed_in(type)_Pubs and bars'])

    listedIn[typeOfListedIn]=1

    st.write("Is Online Order Available ? ")
    order = st.radio(
        "Pick One",
        ('Yes', 'No'))
    if order =="No":
        onlineOrder['online_order_Yes'] = 0


    st.write("Is Table Booking Available ? ")
    booking = st.radio(
        "Select Yes or No",
        ('Yes', 'No'))
    if booking =="No":
        bookTable['book_table_Yes'] = 0

    clicked = st.button("Submit the Values")

    if clicked:
        dictForTest = {**multipleTypes,**totalCuisines,**approxCost,**onlineOrder,**bookTable,**location,**restType,**listedIn}
        #preparing dataframe for testing 
        testData = pd.DataFrame(dictForTest,index=[0])
        # load_model = pickle.load(open('RandomForestZomatoModel.pkl', 'rb'))
        # loaded_model = joblib.load('RandomForestZomatoModel.joblib')

    # Load the model from the file
        with open('logreg.pkl', 'rb') as model_file:
            loaded_model = pickle.load(model_file)


        newPrediction = loaded_model.predict(testData)
        predProb = loaded_model.predict_proba(testData)
        successPercent = predProb[0][1] * 100
        st.subheader("Success Percentage of Your Restaurant is {:.2f}".format(successPercent))

    # if st.button("next page", key="button_2"):
    #     st.write(" Button Clicked!")
    #     st.experimental_set_query_params(page="page4")


    st.markdown(
        """
        <style>
            div[data-testid="stButton_button_2"] > button {
                position: fixed;
                bottom: 10px;
                right: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
if __name__ == "__main__":
    page3()
