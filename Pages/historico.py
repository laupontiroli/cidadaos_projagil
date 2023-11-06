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

# def main():
#     st.markdown(
#         """
#         <style>
#         body {
#             background-color: #8470ff;
#             overflow: hidden;
#         }
#         .menu-lateral {
#             position: fixed;
#             top: 0;
#             left: 0;
#             width: 200px;
#             height: 100%;
#             background-color: #2e2e2e;
#             color: white;
#             padding: 20px;
#         }
#         .menu-lateral a {
#             display: block;
#             color: white;
#             text-decoration: none;
#             margin-bottom: 15px;
#         }
#         .menu-lateral a:hover {
#             color: #8470ff;
#         }
#         .menu-lateral .logo {
#             font-size: 24px;
#             font-weight: bold;
#             margin-bottom: 30px;
#         }
#         .conteudo {
#             margin-left: 230px;
#             padding: 20px;
#         }
#         .titulo {
#             font-size: 30px;
#             margin-bottom: 20px;
#             color: #2e2e2e;
#         }
#         .subtitulo {
#             font-size: 20px;
#             margin-bottom: 10px;
#             color: #2e2e2e;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     st.sidebar.markdown(
#         """
#         <div class="menu-lateral">
#             <div class="logo">Denúncias Urbanas</div>
#             <a href="#inicio">Início</a>
#             <a href="#reportar">Reportar</a>
#             <a href="#acompanhar">Acompanhar Resolução</a>
#             <a href="#fale-conosco">Fale Conosco</a>
#             <a href="#sobre">Sobre</a>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
st.markdown("<h1 id='inicio' class='titulo'>Acompanhe a resolução de algum problema</h1>", unsafe_allow_html=True)
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: rgba(53, 219, 217,0.6);
    }
    [data-testid="stSidebarNav"]::before {
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

# if __name__ == '__main__':
# main()