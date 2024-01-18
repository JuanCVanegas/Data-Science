import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import time
import plotly.express as px


import warnings
warnings.filterwarnings('ignore')


github_csv_url_1 = "https://raw.githubusercontent.com/JuanCVanegas/Data-Science/main/ventas_dataset.csv"
initial_data = pd.read_csv(github_csv_url_1)

github_csv_url_2 = "https://raw.githubusercontent.com/JuanCVanegas/Data-Science/main/ventas_dataset_corregido.csv"
clean_data = pd.read_csv(github_csv_url_2)

github_csv_url_3 = "https://raw.githubusercontent.com/JuanCVanegas/Data-Science/main/ventas_dataset_final.csv"
final_data = pd.read_csv(github_csv_url_3)

initial_data.columns = initial_data.columns.str.capitalize()
clean_data.columns = clean_data.columns.str.capitalize()
final_data.columns = final_data.columns.str.capitalize()

st.set_page_config(
    page_title = 'Ventas e-Commerce',
    page_icon = '📊',
    layout = 'wide'
)

st.title(':blue[_Ventas e-Commerce_] 🖥️')
seccion = st.selectbox(":blue[**Sección** 💡]", ("Análisis Exploratorio","Clasificación","Predicción"))
variable = None  # Inicializar la variable aquí
if seccion == "Análisis Exploratorio":
    variable = st.selectbox(":green[**Variable** 💡]", ("Ventas", "Precio", "Publicidad", "Competencia", "Temporada", "Promoción"))

placeholder = st.empty()

if seccion == "Análisis Exploratorio" :
    
    if variable == "Ventas":
        fig1 = px.histogram(initial_data, x='Ventas', title='Distribución de Ventas', labels={'Ventas': 'Ventas'}, template='plotly_white', opacity=0.7, color_discrete_sequence=['#3498db'], barmode='overlay')
        fig2 = initial_data['Ventas'].describe()
    if variable == "Precio":   
        fig1 = px.histogram(initial_data, x='Precio', title='Distribución de Precio', labels={'Precio': 'Precio'}, template='plotly_white', opacity=0.7, color_discrete_sequence=['#3498db'], barmode='overlay')
        fig2 = initial_data['Precio'].describe()
    if variable == "Publicidad":
        fig1 = px.histogram(initial_data, x='Publicidad', title='Distribución de Publicidad', labels={'Publicidad': 'Publicidad'}, template='plotly_white', opacity=0.7, color_discrete_sequence=['#3498db'], barmode='overlay')
        fig2 = initial_data['Publicidad'].describe()
    if variable == "Competencia":
        fig1 = px.pie(initial_data, names='Competencia', title='Competencia', labels={'Competencia': 'Competencia'}, template='plotly_white', color_discrete_sequence=['#3498db'])
        fig2 = initial_data['Competencia'].describe()
    if variable == "Temporada":
        fig1 = px.pie(initial_data, names='Temporada', title='Temporada', labels={'Temporada': 'Temporada'}, template='plotly_white', color_discrete_sequence=['#3498db'])
        fig2 = initial_data['Temporada'].describe()
    if variable == "Promoción":
        fig1 = px.pie(initial_data, names='Promocion', title='Promoción', labels={'Promoción': 'Promoción'}, template='plotly_white', color_discrete_sequence=['#3498db'])
        fig2 = initial_data['Promocion'].describe()
    
    with placeholder.container():
        fig_col1, fig_col2 = st.columns(2)

        with fig_col1:
            st.markdown("### :blue[Figure 1] 📊")
            st.write(fig1)

        with fig_col2:
            st.markdown("### :blue[Figure 2] 📈")
            st.write(fig2)

elif seccion == "Clasificación":
    image_url_1 = "https://raw.githubusercontent.com/JuanCVanegas/Data-Science/main/Experiment%20Summary.png"
    image_url_2 = "https://raw.githubusercontent.com/JuanCVanegas/Data-Science/main/Model%20Comparison.png"
    image_url_3 = "https://raw.githubusercontent.com/JuanCVanegas/Data-Science/main/SVM.png"

    st.image([image_url_1, image_url_2, image_url_3], caption=['Experiment Summary', 'Model Comparison', 'SVM'], width=600)

elif seccion == "Predicción":
    image_url_1 = "https://raw.githubusercontent.com/JuanCVanegas/Data-Science/main/Regression%20Model%20Comparison.png"
    image_url_2 = "https://raw.githubusercontent.com/JuanCVanegas/Data-Science/main/R2.png"


    st.image([image_url_1, image_url_2], caption=['Model Comparison', 'Negative R2'], width=600)


 
 
    
        