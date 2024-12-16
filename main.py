import streamlit as st

# Set the title of the web page
st.title("Simple Web Form with Streamlit")

# Set a header
st.header("User Information Users")

# Text input for name
name = st.text_input("Enter your name: ")

# Dropdown menu for selecting an option
options = ["Option 1", "Option 2", "Option 3"]
selected_option = st.selectbox("Choose an Option:", options)

# Slider for selecting a value 
slider_value = st.slider("Select as value", 1, 100, 50)

#Radio button for selecting gender
gender = st.radio("Select your gender: ", ("Male, Female"))

# Date picker for selecting birthdate

# Submit button
if st.button("Sumbit"):
    st.write(f"Name: {name}")
    st.write(f"Selected Option: {selected_option}")
    st.write(f"Slider Value: {slider_value}")
    st.write(f"Gender: {gender}")

# Additional information
st.subheader("Summary")
st.write("Fill out the form above and click the Sumbit button")
# Footer

