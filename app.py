import pandas as pd
import plotly.express as px
import streamlit as st
# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.header("Análisis de Datos de Vehículos")

# Botón para construir un histograma
hist_button = st.button('Construir histograma')

if hist_button:
    # Al hacer clic en el botón, escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer", title="Histograma del Odometer((mediciòn de Kilómetros))")

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    # Al hacer clic en el botón, escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión (por ejemplo, odometer vs. price)
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersión: Odometer vs Price")

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)


# Casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    # Si la casilla de verificación está seleccionada, escribir un mensaje
    st.write('Construyendo un histograma para la columna "odometer"')

    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer", title="Histograma del Odometer")

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    # Si la casilla de verificación está seleccionada, escribir un mensaje
    st.write('Construyendo un gráfico de dispersión para "odometer" vs "price"')

    # Crear un gráfico de dispersión (por ejemplo, odometer vs. price)
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersión: Odometer vs Price")

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)