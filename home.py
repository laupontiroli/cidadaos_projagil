import streamlit as st
from utils import *

st.set_page_config(page_title='Reporta Cidade', page_icon=':cityscape:', layout='wide', initial_sidebar_state='auto')

st.title('Reporta Cidade')

st.sidebar.title('Menu')

st.write('## Algum problema na cidade para reportar?')

st.write("""Buracos nas ruas e avenidas?""")
st.write(' Falta de sinalização?')
st.write(' Postes queimados?')
st.write('Calçadas obstruídas?')
st.write('Vazamento de água ou esgoto? ')
st.write(' Falta de rampas para deficientes?')
st.write('...')

st.write('### Para reportar clique em "reportar" na aba do menu!')