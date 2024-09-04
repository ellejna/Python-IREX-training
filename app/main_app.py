import streamlit as st

if st.button("Click Me!"):
    st.write("Button clicked!")

if st.checkbox("Check me!"):
    st.write("Button checked successfully!")

# don't forget to use cd to go into a file,
# and also terminate a terminal if you don't need it

user_input = st.text_input("Enter your name: ")
st.write("Your name is: ", user_input)

age = st.number_input("Enter your age: ", min_value=1, max_value=200)
st.write(f"Your age is: {age}")

message = st.text_area("Enter your message: ")
st.write(f"Your message is: {message}")

# Radio buttons

choice = st.radio("Would you like to play again?", ["Yes", "No", "Maybe"])
st.write(f"Your answer was {choice}")

#showing the user whether it was successful or not
if st.button("Success"):
    st.success("Operation was successful!")
else:
    st.error("Operation was not successful!")

# exception message
try:
    1/0
except Exception as e:
    st.exception(e)
    
