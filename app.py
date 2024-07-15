import pandas as pd
import plotly.express as px
import streamlit as st

# Cabeçalho do aplicativo
st.header("Análise de Dados de Anúncios de Vendas de Carros")

car_data = pd.read_csv('C:\\Users\\User\\Desktop\\Data Science\\Tripleten\\sprint_5\\vehicles.csv') # lendo os dados

hist_button = st.button('Criar histograma') # criar um botão
     
if hist_button: # se o botão for clicado
     # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
     # criar um histograma
    fig = px.histogram(car_data, x="odometer")
     
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Botão para criar gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    # Mensagem ao clicar no botão
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    # Criar um gráfico de dispersão
    fig = px.scatter(car_data, x='odometer', y='price', color='condition')
    
    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)