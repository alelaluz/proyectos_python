import pyshorteners
import streamlit as st


def acorta_url(url):
    """ Funcion que le pasamos como input la url a acortar, creando un objeto de la libreria pyshorteners, 
llamando al metodo tinyurl.short que nos acorta la url pasandole la url a acortar.

    Args:
        url (url):url a acortar

    Returns:
        url_acortada: Retorna url acortada
    """
    o = pyshorteners.Shortener()
    url_acortada = o.tinyurl.short(url)
    return url_acortada


# Usamos stremamlit  para crear la App web
st.set_page_config(page_title="URL Shortener",
                   page_icon="✏️", layout="centered")
st.image("img/estructura-url.png", use_column_width=True)
st.title("ACORTAMIENTO DE URL")
url = st.text_input("Ingrese la URL")
if st.button("Generar la nueva URL"):
    st.write("URL final: ", acorta_url(url))
