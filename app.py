import streamlit as st
import pandas as pd
#from matplotlib import pyplot as plt
df = pd.read_csv('vehicles_us.csv')

st.write("Hello")

# load data
st.table(df.head())

# data clean

# plot some graph