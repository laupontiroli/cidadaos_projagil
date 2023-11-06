import streamlit as st

def obter_info_reclamacao(codigo):
    reclamacoes = {
        "12345": {
            "resumo": "Infraestrutura danificada",
            "descricao": "Buraco com raio de 1m no meio da rua",
            "localizacao": "Rua Quata",
            "status": "Em andamento",
            "timeline": [
                {"data": "01/10/2023", "hora": "09:00:00", "acao": "Reclamação registrada"},
                {"data": "05/10/2023", "hora": "10:30:00", "acao": "Reclamação em análise pelos órgãos públicos"},
                {"data": "10/10/2023", "hora": "11:45:00", "acao": "Trabalhadores foram enviados ao local"} ]}}

    return reclamacoes.get(codigo, None)


st.markdown("<h1 id='inicio' class='titulo'>Acompanhe a resolução de algum problema</h1>", unsafe_allow_html=True)
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
info_reclamacao = obter_info_reclamacao(codigo_reclamacao)

if info_reclamacao:
    st.markdown("<h2 class='subtitulo'>Detalhes da reclamação</h2>", unsafe_allow_html=True)
    st.write(f"Resumo do problema: {info_reclamacao['resumo']}")
    st.write(f"Descrição: {info_reclamacao['descricao']}")
    st.write(f"Localização: {info_reclamacao['localizacao']}")
    st.write(f"Status: {info_reclamacao['status']}")
    
    st.markdown("<h2 class='subtitulo'>Timeline da reclamação</h2>", unsafe_allow_html=True)
    for evento in info_reclamacao['timeline']:
        st.write(f"Dia: {evento['data']} - Hora: {evento['hora']} - Ação: {evento['acao']}")
else:
    if codigo_reclamacao:
        st.error("Reclamação não encontrada. Verifique o código inserido.")

