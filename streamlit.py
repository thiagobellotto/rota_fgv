import streamlit as st
st.set_page_config(page_title="Rota 2030 - FGV", 
    page_icon="https://logodownload.org/wp-content/uploads/2016/09/fgv-logo-0.png",
    layout="centered")

st.title("Rota 2030 - FGV")

frame = '''<iframe title="Rota_2030_v3 - Parte 1 - Preferencias" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiMDBkYjIxNDktZjU0My00NTdiLTk4MTEtMjY3M2Q2YWU0MGZmIiwidCI6ImQ2MzljZTdiLTBiNjUtNGJmOS1iNTk2LTllYzI2OWM1OTYxOSJ9" frameborder="0" allowFullScreen="true"></iframe>'''

footer="""<style>
a:link , a:visited{
color: black;
background-color: transparent;
text-decoration: underline;
}
a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by <a style='display: block; color: black; text-align: center;' href="https://www.linkedin.com/in/thiago-bellotto/" target="_blank">Thiago Bellotto</a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

# display an embeddded from power bi
st.markdown(frame, unsafe_allow_html=True)
