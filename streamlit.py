import streamlit as st

st.set_page_config(
    page_title="Rota 2030 - FGV",
    page_icon="https://logodownload.org/wp-content/uploads/2016/09/fgv-logo-0.png",
    layout="centered",
)

st.title("Rota 2030 - FGV - Fase 2")

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
st.subheader("Matriz Importância X Desempenho")
url_1 = f'<iframe title="fase2-grafico1-final" width="{width}" height="{height}" src="https://app.powerbi.com/view?r=eyJrIjoiYTVmODU3NzYtNWRhYi00YWZjLThhNGEtODk1OTY5YTlhZDRlIiwidCI6ImQ2MzljZTdiLTBiNjUtNGJmOS1iNTk2LTllYzI2OWM1OTYxOSJ9&pageName=ReportSection4002c908007b02add658" frameborder="0" allowFullScreen="true"></iframe>'
grafico_1 = f"""{url_1}"""
st.markdown(grafico_1, unsafe_allow_html=True)

st.subheader("Desempenho em todos os atributos por ferramentaria")
url_2 = f'<iframe title="fase2-grafico2-final" width="{width}" height="{height} src="https://app.powerbi.com/view?r=eyJrIjoiNTQ1ZWYzNmMtY2Q3OC00ODg5LTkzYWMtNDY2OGViYTc0ZGUwIiwidCI6ImQ2MzljZTdiLTBiNjUtNGJmOS1iNTk2LTllYzI2OWM1OTYxOSJ9&pageName=ReportSectionbd98154115c8c014dd88" frameborder="0" allowFullScreen="true"></iframe>'
grafico_2 = f"""{url_2}"""
st.markdown(grafico_2, unsafe_allow_html=True)

st.subheader("Desempenho em todos as ferramentarias por atributo")
url_3 = f'<iframe title="fase2-grafico3-final" width="{width}" height="{height}" src="https://app.powerbi.com/view?r=eyJrIjoiZGM0ZTE3Y2MtN2JmZS00Y2ZkLTk5MjMtMzY2YzljOWU5YjQzIiwidCI6ImQ2MzljZTdiLTBiNjUtNGJmOS1iNTk2LTllYzI2OWM1OTYxOSJ9&pageName=ReportSection57869b2859ac5e89e618" frameborder="0" allowFullScreen="true"></iframe>'
grafico_3 = f"""{url_3}"""
st.markdown(grafico_3, unsafe_allow_html=True)
