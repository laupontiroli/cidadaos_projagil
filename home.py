import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events


st.set_page_config(page_title='Reporta Cidade', page_icon=':cityscape:', layout='wide', initial_sidebar_state='auto')

loc_button = Button(label="Get Location")
loc_button.js_on_event("button_click", CustomJS(code="""
    navigator.geolocation.getCurrentPosition(
        (loc) => {
            document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
        }
    )
    """))
result = streamlit_bokeh_events(
    loc_button,
    events="GET_LOCATION",
    key="get_location",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_LOCATION" in result:
        st.write(result.get("GET_LOCATION"))

import streamlit as st
from utils import *


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