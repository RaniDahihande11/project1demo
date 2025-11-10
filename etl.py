import streamlit as st
import pandas as pd

data = {
    "Task":['Extract','Transform','Load'],
    "Status":["Completed","Processing","Pending"]
}

df = pd.DataFrame(data)
st.title("Streamit App")
st.write(df)