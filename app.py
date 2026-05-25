import streamlit as st
from supabase import create_client

url = "https://uxgvgumfqbvsknhdjjnu.supabase.co"
key = "sb_publishable_uMTn1gbS1AX5MIbmTa8nrA_-i2e8a7s"

supabase = create_client(url, key)

st.title("Registro de Delitos")

tipo = st.text_input("Tipo de delito")
fecha = st.date_input("Fecha")

if st.button("Guardar"):

    datos = {
        "tipo_delito": tipo,
        "fecha": str(fecha)
    }

    supabase.table("Delitos").insert(datos).execute()

    st.success("Dato guardado")