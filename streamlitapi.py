import pickle
import streamlit as st

# Load the model
model = pickle.load(open("C:/Users/PC/Desktop/ML PROJECTS/random_forest_model.pkl", 'rb'))

def main():
    st.title("Car Pricing Prediction")

    # Text input fields (with conversion)
    Year = st.text_input("Year (e.g. 2015)")
    Kms_Driven = st.text_input("Kms Driven (e.g. 45000)")
    Owner = st.text_input("Number of Previous Owners (e.g. 1)")

    Fuel_Type_Diesel = st.text_input("Fuel_Type_Diesel (1 for Diesel, 0 otherwise)")
    Fuel_Type_Petrol = st.text_input("Fuel_Type_Petrol (1 for Petrol, 0 otherwise)")
    Seller_Type_Individual = st.text_input("Seller_Type_Individual (1 for Individual, 0 otherwise)")
    Transmission_Manual = st.text_input("Transmission_Manual (1 for Manual, 0 otherwise)")

    # Prediction
    if st.button("Predict"):
        makeprediction = model.predict([[Year, Kms_Driven, Owner, Fuel_Type_Diesel, Fuel_Type_Petrol,
        Seller_Type_Individual, Transmission_Manual]])
        output = round(makeprediction[0], 2)
        st.success("You Can Sell Your Car at {}".format(output))

if __name__ == '__main__':
 main()
