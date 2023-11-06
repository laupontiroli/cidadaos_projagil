import streamlit as st 
import os 
import api_utils as uts
from time import sleep 

def save_uploaded_file(uploadedfile):
  with open(os.path.join("./photos",uploadedfile.name),"wb") as f:
     f.write(uploadedfile.getbuffer())
  return True

st.title('Informações sobre o Problema')

st.divider()
with st.form("Formulário",clear_on_submit=True):
    col1, col2 = st.columns([2,2]) 

    with col1: 
        bairro = st.text_input("Digite o Nome do Bairro",placeholder="Nome do Bairro")
        rua = st.text_input("Digite o Nome da Rua",placeholder="Nome da rua")
        foto = st.file_uploader("Foto do problema")
        
    with col2: 
        problema_tipo = st.selectbox("Tipo de problema",("Buraco na via","Buraco na calçada","Luz queimada",'Farol queimado','Outro'))
        if problema_tipo == "Outro":
            problema_tipo = st.text_input("Escreva aqui o problema em poucas palavras")
        urgencia = st.radio("Nível de urgência",('Extrema','Mediana','Mínima'))
        problema_descricao =st.text_area("Relate o problema",placeholder="Detalhe bem sobre o problema, desde quando, dificuldades que está causando, etc.")
        data_inicio = st.date_input("Desde quando este problema existe ou desde quando você o percebeu?",format='DD/MM/YYYY')



    if st.form_submit_button("Enviar Formulário"):
        if foto:
            save_uploaded_file(foto)
        data = {'bairro': bairro ,'rua': rua, 'problema_tipo':problema_tipo, 'urgencia': urgencia, 'problema_descricao': problema_descricao,'data_inicio': data_inicio}
        file= {'foto':open(f'./photos/{foto.name}','rb')}
        salvou, mensagem = uts.registra_problema(data,file)
        if salvou: 
            st.balloons()
            st.success(f'Seu problema foi reportado com Sucesso! Segue o identificador do seu problema para que você possa acompanhá-lo {mensagem}')
                
                

