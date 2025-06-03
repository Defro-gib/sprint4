import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pyarrow as pa



# Load the dataset
df = pd.read_csv('vehicles_us.csv')

duplicated_rows = df[df.duplicated()]
print(f"Number of duplicate rows: {duplicated_rows.shape[0]}")
df.drop_duplicates(inplace=True)

print("Missing cylinders before:", df['cylinders'].isna().sum())

# Impute missing 'cylinders' using the median per model and year
df['cylinders'] = df.groupby(['model', 'year'])['cylinders'].transform(
    lambda x: x.fillna(x.median())
)

# Check again
print("Missing cylinders after:", df['cylinders'].isna().sum())

# Convert 'price' column to numeric, forcing errors to NaN
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Handle NaN values in 'price' (optional: you can fill or drop them)
df['price'] = df['price'].fillna(0)  # Or use df.dropna(subset=['price']) to remove rows

# Ensure 'price' column is of type float64
df['price'] = df['price'].astype('float64')

# Convert the cleaned DataFrame to a PyArrow Table
try:
    df_arrow = pa.Table.from_pandas(df)
    print("Conversion successful!")
except Exception as e:
    print("Error during conversion:", e)



# Clean missing values
df['model_year'] = df['model_year'].fillna('N/A')
df['cylinders'] = df['cylinders'].fillna('N/A')
df['odometer'] = df['odometer'].fillna('N/A')
df['paint_color'] = df['paint_color'].fillna('N/A')
df['is_4wd'] = df['is_4wd'].fillna('N/A')

df['model_year'] = df['model_year'].fillna('N/A')
df['cylinders'] = df['cylinders'].fillna('N/A')
df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce').fillna(0)  # Ensure numeric type for odometer
df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)  # Ensure numeric type for price
df['paint_color'] = df['paint_color'].fillna('N/A')
df['is_4wd'] = df['is_4wd'].fillna('N/A')



df.info()
df.head()


# Convert 'date_posted' to datetime format (if necessary)
df['date_posted'] = pd.to_datetime(df['date_posted'], errors='coerce')




# Create the Streamlit app
st.title("Vehicle Listings Analysis")

# Add a header
st.header("Explore Vehicle Listings Dataset")

# Show dataset info (optional)
if st.checkbox('Show raw data'):
    st.subheader('Raw Dataset')
    st.write(df.head())

# Create the scatter plot
scatter_fig = px.scatter(df, 
                         x='days_listed', 
                         y='model_year', 
                         color='type',
                         title='Scatter Plot of Days Listed vs Model Year',
                         labels={'days_listed': 'Days Listed', 'model_year': 'Model Year'},
                         size_max=10)

# Create the histogram
hist_fig = px.histogram(df, 
                        x='days_listed', 
                        nbins=20,
                        title='Distribution of Days Listed',
                        labels={'days_listed': 'Days Listed'})

# Use make_subplots to create a figure with two rows for both scatter and histogram
fig = make_subplots(rows=2, cols=1, 
                    subplot_titles=("Scatter Plot of Days Listed vs Model Year", 
                                    "Histogram of Days Listed"))

# Add scatter plot to the first row
fig.add_trace(go.Scatter(x=scatter_fig.data[0].x, 
                         y=scatter_fig.data[0].y,
                         mode='markers',
                         marker=dict(color=scatter_fig.data[0].marker.color),
                         name='Scatter'),
              row=1, col=1)

# Add histogram to the second row
fig.add_trace(go.Histogram(x=hist_fig.data[0].x,
                           nbinsx=20,
                           name='Histogram'),
              row=2, col=1)

# Update layout for the combined figure
fig.update_layout(height=800, 
                  title_text="Scatter Plot and Histogram of Days Listed",
                  showlegend=False)

# Display the combined plot in Streamlit
st.plotly_chart(fig)

# Optional: Add interactive checkbox for showing individual plots
if st.checkbox('Show only scatter plot'):
    st.plotly_chart(scatter_fig)

if st.checkbox('Show only histogram'):
    st.plotly_chart(hist_fig)
