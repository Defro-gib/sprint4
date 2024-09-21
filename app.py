import streamlit as st
import pandas as pd
#from matplotlib import pyplot as plt
df = pd.read_csv('vehicles_us.csv')

st.write("Hello")

# load data
st.table(df.head('Car Sales'))

# data clean

# plot some graph
import pandas as pd
import plotly.express as px
#from matplotlib import pyplot as plt
df = pd.read_csv('vehicles_us.csv')

df['model_year']= df['model_year'].fillna('N/A')
df['cylinders']= df['cylinders'].fillna('N/A')
df['odometer']= df['odometer'].fillna('N/A')
df['paint_color']= df['paint_color'].fillna('N/A')
df['is_4wd']= df['is_4wd'].fillna('N/A')



df.info()
df.head()

fig = px.scatter(df, x= 'model_year', y= 'days_listed')
fig.show()


#df.plot(kind='hist')


#plt.show()