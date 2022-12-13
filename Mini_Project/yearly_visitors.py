# 1. import libraries
import numpy as np
import pandas as pd
import plotly.express as px # simple graphs
import plotly.graph_objects as go # complex graphs
import streamlit as st

# common variables
years = list(range(2014,2021))

# 2. create function to clean data
def clean_dataset(df):
    df.set_index('Country', inplace=True) # set country as index
    df['Total'] = df[years].sum(axis=1)   # add a total column to the dataframe
    return df

# 3. create function to load data
st.cache()                                # helps to make the app faster
def load_dataset():
    df = pd.read_csv('Data/Country Wise Yearly Visitors.csv',skiprows=20, skipfooter=2)
    df = clean_dataset(df)
    return df

# 4. setup basic UI
st.title("Visitors from Countries to India")
with st.spinner("loading dataset"):                          # show a loading message
    df = load_dataset()
    # st.balloons()        

if st.sidebar.checkbox("Show full dataframe"):          # show raw data if checkbox is checked
    st.write(df)

# 5. give user option to select columns
st.sidebar.header("Visitors from Countries to India")
country = df.index.tolist()
sel_country = st.sidebar.selectbox("Country", country)

# graph
st.header(f'Immigration from {sel_country} to India')
country = df.loc[sel_country, years] # subset
fig = px.line(country, x=country.index, y=country.values)
st.plotly_chart(fig)

st.sidebar.header("Select multiple countries to visualize")
sel_countries = st.sidebar.multiselect("Countries", country)
if len(sel_countries)>1:
    st.header(f'Comparing countries {", ".join(sel_countries)}')
    df_countries = df.loc[sel_countries, years].T # subset
    fig = px.bar(df_countries, x=years, y=sel_countries)
    st.plotly_chart(fig)
else:
    st.warning('Please select at least 2 countries for comparison')
# 6. give user option display graphs

# 0. Run the app run the command below
# streamlit run home.py