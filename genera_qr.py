import qrcode
import streamlit as st

# Definimos el path donde se va a almacenar el Qr, dando nombre a la imagen del qr generado como codigo_final_qr.png
filename = "codigos_imagen/codigo_final_qr.png"


def generar_qr(url, filename):
    """Funcion donde genera el codigo qr a partir de una url,
    creamos un objeto o_qr.
    añadimos los datos de nuestra url al qr ( qr.add_data(url), qr.make(fit=True))
    generamos la imagen con el metodo make_image  de la libreria qrcode  y la guardamos con el metodo save.


    Args:
        url (url): pasamos la url a convertir
        filename (filename): pasamos el path donde se guarda el qr
    """
    o_qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    o_qr.add_data(url)
    o_qr.make(fit=True)

    imagen_qr = o_qr.make_image(fill_color="black", back_color="white")
    imagen_qr.save(filename)


# Usamos stremamlit  para crear la App web
st.set_page_config(page_title="Generador de QR",
                   page_icon="😎", layout="centered")
st.image("img/imagen_codigo.jpg", use_column_width=True)
st.title("Generador de QR")
url = st.text_input("Ingrese la URL a generar")

if st.button("Generar codigo QR"):
    generar_qr(url, filename)
    st.image(filename, use_column_width=True)
    with open(filename, "rb") as f:
        image_data = f.read()
    download = st.download_button(
        label="Download QR", data=image_data, file_name="qr_generated.png")
