import streamlit as st

st.set_page_config(
    page_title="Rota 2030 - FGV",
    page_icon="https://logodownload.org/wp-content/uploads/2016/09/fgv-logo-0.png",
    layout="centered",
)

st.title("Rota 2030 - FGV")

footer = """<style>
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
st.markdown(
    """ <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """,
    unsafe_allow_html=True,
)

width = 1200
height = 750

# display an embeddded from power bi 
url = f'<iframe style="position:absolute; height:100%; width:100%; border: none" title="Rota_2030_v3_Gráfico_1" width="{width}" height="{height}" src="https://app.powerbi.com/view?r=eyJrIjoiOTYyMjNlYTgtYTMwNi00MTJjLTkxM2MtNjFmNDU1ZTMzZDlmIiwidCI6Ijc5ZjZiNjM5LWFiMTItNDI4MC04MDc3LWJkYmVlZjg2OWIzMyIsImMiOjR9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>'
grafico = f"""{url}"""
st.markdown(grafico, unsafe_allow_html=True)
