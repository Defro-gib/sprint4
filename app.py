import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Impute missing 'cylinders' using median grouped by model and year
df['cylinders'] = df.groupby(['model', 'year'])['cylinders'].transform(
    lambda x: x.fillna(x.median())
)

# Convert necessary columns and fill remaining missing values
df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)
df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce').fillna(0)
df['model_year'] = df['model_year'].fillna('N/A')
df['paint_color'] = df['paint_color'].fillna('N/A')
df['is_4wd'] = df['is_4wd'].fillna('N/A')

# Convert date_posted to datetime
df['date_posted'] = pd.to_datetime(df['date_posted'], errors='coerce')

# --- Streamlit App ---
st.title("Vehicle Listings Analysis")
st.header("Explore Vehicle Listings Dataset")

# Show raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw Dataset')
    st.write(df.head())

# Scatter plot
scatter_fig = px.scatter(
    df, x='days_listed', y='model_year', color='type',
    title='Scatter Plot of Days Listed vs Model Year',
    labels={'days_listed': 'Days Listed', 'model_year': 'Model Year'}
)

# Histogram
hist_fig = px.histogram(
    df, x='days_listed', nbins=20,
    title='Histogram of Days Listed',
    labels={'days_listed': 'Days Listed', 'count': 'Frequency'}
)

# Combined plot with subplots
fig = make_subplots(
    rows=2, cols=1, subplot_titles=(
        "Scatter Plot of Days Listed vs Model Year",
        "Histogram of Days Listed"
    )
)

# Add traces
fig.add_trace(
    go.Scatter(
        x=scatter_fig.data[0].x,
        y=scatter_fig.data[0].y,
        mode='markers',
        marker=dict(color=scatter_fig.data[0].marker.color),
        name='Scatter Plot'
    ),
    row=1, col=1
)

fig.add_trace(
    go.Histogram(
        x=hist_fig.data[0].x,
        nbinsx=20,
        name='Histogram'
    ),
    row=2, col=1
)

# Update layout with proper labels
fig.update_layout(
    height=800,
    title_text="Scatter Plot and Histogram of Days Listed",
    showlegend=False
)
fig.update_xaxes(title_text="Days Listed", row=2, col=1)
fig.update_yaxes(title_text="Model Year", row=1, col=1)
fig.update_yaxes(title_text="Frequency", row=2, col=1)

# Display in Streamlit
st.plotly_chart(fig)

# Optionally show single charts
if st.checkbox('Show only scatter plot'):
    st.plotly_chart(scatter_fig)

if st.checkbox('Show only histogram'):
    st.plotly_chart(hist_fig)