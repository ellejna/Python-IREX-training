import pandas as pd
import streamlit as st

st.header("Welcome to Displaying Dataframe 101")
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Dave"],
    "Age": [28, 22, 23, 24],
    "city": ["New York", "San Francisco", "Los Angeles", "San Francisco",]
})

st.write(df)
