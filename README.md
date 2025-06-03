# sprint4
 Vehicle Listings Analysis Tool
📊 Sprint 4 Project – Exploratory Data Analysis & Web Application
🔍 Project Overview
This project is a Streamlit web application designed to analyze and visualize data from used vehicle listings. It aims to provide insights into vehicle characteristics such as model year, number of days listed, vehicle type, and more. By exploring this data interactively, users can uncover trends and better understand the dynamics of vehicle listings over time.
Key Features
Key Features
Scatter Plot
Visualizes the relationship between how long vehicles are listed and their model year, color-coded by vehicle type.

Histogram
Displays the distribution of the number of days vehicles remain listed.

Interactive Filters
Allows users to filter the data to customize visualizations based on their preferences.
 Exploratory Data Analysis (EDA)
The EDA was conducted in a Jupyter Notebook (eda.ipynb). It includes:

Data cleaning (handling missing values and duplicates)

Descriptive statistics and visualizations

Group-wise imputation using groupby for missing cylinders values

Charts with titles and axis labels

Intermediate conclusions based on data insights

Example EDA Highlights:

Vehicles with more recent model years tend to be listed for fewer days.

Most listings fall within a certain range of listing duration.

cylinders were imputed using a groupby approach on model and year.

🧪 Technologies Used
Streamlit – Building the interactive web app

Pandas – Data manipulation and cleaning

Plotly Express – Creating interactive and visually appealing charts

Jupyter Notebook – Performing EDA and data preprocessing
URL link: https://sprint4-b3k3.onrender.com/

Conclusion
This project successfully demonstrates how exploratory data analysis (EDA) and interactive visualization can provide valuable insights into used vehicle listings. Through the use of a Streamlit web app, users can explore listing trends, vehicle characteristics, and distribution patterns. Missing values were handled thoughtfully, including an imputation technique using grouped medians for cylinders. The tool is practical, extensible, and sets the foundation for future enhancements such as predictive modeling or deeper market analysis.