import pandas as pd
import streamlit as st

st.write('Welcome to AVD')

data = {
    "Task": ["Extract2", "Transform", "Load"],
    "Status": ["Completed", "InProgress", "Pending"]
}

df = pd.DataFrame(data)
st.write("ETL Processing Status : ", df)
