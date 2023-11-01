import streamlit as st 
import os 
import api_utils as uts

def save_uploaded_file(uploadedfile):
  with open(os.path.join("./photos",uploadedfile.name),"wb") as f:
     f.write(uploadedfile.getbuffer())
  return st.success("Saved file :{} in photos".format(uploadedfile.name))

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


if st.button("Enviar Formulario"):
    if foto:
            save_uploaded_file(foto)
    data = {'bairro': bairro ,'rua': rua, 'problema_tipo':problema_tipo, 'urgencia': urgencia, 'problema_descricao': problema_descricao,'data_inicio': data_inicio}
    file= {'foto':open(f'./photos/{foto.name}','rb')}
    salvou = uts.registra_problema(data,file)
    st.write(salvou)
    


