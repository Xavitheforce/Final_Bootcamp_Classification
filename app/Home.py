import streamlit as st

st.set_page_config(
    page_title="馃拕Final Project",
)

st.title("馃槇 Proyecto Final")

dict = {
    "Javier M铆guelez": "https://github.com/Xavitheforce",
    "Juan Medina": "https://github.com/jmedina28",
    "Diego de Santos": "https://github.com/Diegodesantos1"
}
st.write('''馃憗锔忦煈勷煈侊笍
    Tras la realizaci贸n del curso de Data Science, nos hemos dispuesto a realizar un proyecto final.
    El proyecto consiste en la creaci贸n de una aplicaci贸n web que muestre los resultados de dos modelos, uno de regresi贸n y otro de clasificaci贸n.
    Los autores de este proyecto son los siguientes:''')

for key, value in dict.items():
    st.write(f"馃憠 {key} 馃ザ {value}")