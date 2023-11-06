import streamlit as st

st.set_page_config(page_title='Reporta Cidade', page_icon=':cityscape:', layout='wide', initial_sidebar_state='auto')

st.markdown('<h1 style="color: rgb(47, 194, 192); text-align: center ">Reporta Cidade</h1>', unsafe_allow_html=True)

st.divider()
st.write('### Algum problema na cidade para reportar?')

st.write("""Buracos nas ruas e avenidas?""")
st.write(' Falta de sinalização?')
st.write(' Postes queimados?')
st.write('Calçadas obstruídas?')
st.write('Vazamento de água ou esgoto? ')
st.write(' Falta de rampas para deficientes?')
st.write('...')

st.markdown('### <span style="color:#e74c3c">Para reportar clique no botão abaixo!</span>', unsafe_allow_html=True)


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

st.markdown(
    '''
    <a href="/Reportar" style="display: inline-block; background-color: #e74c3c; color: #000000; text-align: center; padding: 10px 20px; border-radius: 5px; text-decoration: none; font-weight: bold;">Reportar</a>
    ''',
    unsafe_allow_html=True
)