import streamlit as st
st.title("Calculadora de Média")
# Adiciona uma barra lateral
st.sidebar.header("Escolha os números:")
# Adiciona widgets à barra lateral
numero1 = st.sidebar.number_input("Número 1", value=0)
numero2 = st.sidebar.number_input("Número 2", value=0)
# Adiciona um botão na barra lateral
calcular_button = st.sidebar.button("Calcular Média")
# Adiciona widgets ao corpo principal
st.write("## Informações:")
st.write(f"Número 1: {numero1}")
st.write(f"Número 2: {numero2}")
# Executa a ação do botão
if calcular_button:
    media = (numero1 + numero2) / 2
    st.success(f"A média é: {media}")

