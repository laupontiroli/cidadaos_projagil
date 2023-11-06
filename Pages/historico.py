import streamlit as st
from api_utils import get_problema_id

st.markdown("<h1 id='inicio' class='titulo'>Acompanhe a resolução do seu problema</h1>", unsafe_allow_html=True)
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: rgba(53, 219, 217,0.6);
    }
    [data-testid="stSidebarNav"]::before {
        font-weight : 600;
        content: "Menu";
        margin-left: 20px;
        font: Helvica Bold;
        margin-top: 20px;
        font-size: 30px;
        position: relative;
        top: 100px;
        }
</style>
""", unsafe_allow_html=True)

codigo_reclamacao = st.text_input("Insira o código da reclamação:")

if codigo_reclamacao != '':
    achou,info_reclamacao =get_problema_id(codigo_reclamacao)
    print (f'-----------------------{achou}{info_reclamacao}')

    if achou:
        if info_reclamacao == []:
            st.error("Reclamação não encontrada. Verifique o código inserido.")
        if 'erro' in info_reclamacao:
            st.error("Reclamação não encontrada. Verifique o código inserido.")
        else: 
            st.markdown("<h2 class='subtitulo'>Detalhes da reclamação</h2>", unsafe_allow_html=True)
            st.write(f"Descrição do Problema : {info_reclamacao['problemas'][0]['problema_descricao']}")
            st.write(f"O tipo de problema: {info_reclamacao['problemas'][0]['problema_tipo']}")
            st.write(f"Localização: {info_reclamacao['problemas'][0]['rua']},{info_reclamacao['problemas'][0]['bairro']}")
            st.write(f"Status: {info_reclamacao['problemas'][0]['status']}")

    else:
        st.write(info_reclamacao)

