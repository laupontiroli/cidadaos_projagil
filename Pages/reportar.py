import streamlit as st 

st.title('Informações sobre o Problema')

st.divider()

col1, col2 = st.columns([2,2]) 

with col1: 
    bairro = st.text_input("Digite o Nome do Bairro",placeholder="Nome do Bairro")
    rua = st.text_input("Digite o Nome da Rua",placeholder="Nome da rua")
    foto = st.file_uploader("Foto do problema")

with col2: 
    problema_tipo = st.selectbox("Tipo de problema",("Buraco na via","buraco na calçada","luz queimada",'farol queimado','outro'))
    if problema_tipo == "outro":
        problema_tipo = st.text_input("escreva aqui o problema em poucas palavras")
    urgencia = st.radio("nível de urgência",('extrema','mediana','minima'))
    problema_descricao =st.text_area("Relate o problema",placeholder="detalhe bem sobre o problema, desde quando, dificuldades que está causando, etc")
    data_inicio = st.date_input("Desde quando este problema existe ou desde quando você o percebeu?",format='DD/MM/YYYY')


st.button("Enviar Formulario")



