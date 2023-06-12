import streamlit as st
import pandas as pd

df = pd.read_pickle('./AISTOCKADVISOR_IAPT.ipynb')
# Define the layout using Streamlit
st.title("AI Stock Advisor")
st.header("Top 5 and Worst 5 Investments")

# Best to invest in
st.subheader("Best to invest in.")
col1, col2, col3 = st.columns(3)

# Short-Term
with col1:
    st.subheader("Short-Term")
    table_30_day_model = pd.DataFrame({"Name": [str(name) for name in top_best_30Day_Name[:5]]})
    st.dataframe(table_30_day_model)

# Medium-Term
with col2:
    st.subheader("Medium-Term")
    table_60_day_model = pd.DataFrame({"Name": [str(name) for name in top_best_60Day_names[:5]]})
    st.dataframe(table_60_day_model)

# Long-Term
with col3:
    st.subheader("Long-Term")
    table_120_day_model = pd.DataFrame({"Name": [str(name) for name in top_best_120Day_names[:5]]})
    st.dataframe(table_120_day_model)

# Worst to invest in
st.subheader("Worst to invest in.")
col4, col5, col6 = st.columns(3)

# Short-Term
with col4:
    st.subheader("Short-Term")
    table_30_day_model_worst = pd.DataFrame({"Name": [str(name) for name in top_worst_30Day_names[:5]]})
    st.dataframe(table_30_day_model_worst)

# Medium-Term
with col5:
    st.subheader("Medium-Term")
    table_60_day_model_worst = pd.DataFrame({"Name": [str(name) for name in top_worst_60Day_names[:5]]})
    st.dataframe(table_60_day_model_worst)

# Long-Term
with col6:
    st.subheader("Long-Term")
    table_120_day_model_worst = pd.DataFrame({"Name": [str(name) for name in top_worst_120Day_names[:5]]})
    st.dataframe(table_120_day_model_worst)

# Hold Investments
st.subheader("Hold Investments")
col7, col8, col9 = st.columns(3)

# Short-Term
with col7:
    st.subheader("Short-Term")
    table_30_day_hold = pd.DataFrame({"Name": [str(name) for name in top_hold_30Day_names]})
    st.dataframe(table_30_day_hold)

# Medium-Term
with col8:
    st.subheader("Medium-Term")
    table_60_day_hold = pd.DataFrame({"Name": [str(name) for name in top_hold_60Day_names]})
    st.dataframe(table_60_day_hold)

# Long-Term
with col9:
    st.subheader("Long-Term")
    table_120_day_hold = pd.DataFrame({"Name": [str(name) for name in top_hold_120Day_names]})
    st.dataframe(table_120_day_hold)


public_url = ngrok.connect(port='8501')
public_url
