import streamlit as st
from supabase import create_client

st.set_page_config(
    page_title="Registro de Delitos",
    page_icon="🚨",
    layout="centered"
)

url = "https://uxgvgumfqbvsknhdjjnu.supabase.co"
key = "sb_publishable_uMTn1gbS1AX5MIbmTa8nrA_-i2e8a7s"

supabase = create_client(url, key)

st.title("🚨Registro de Delitos")
st.markdown("### Reporta incidentes de forma rápida y sencilla")
tipo = st.selectbox(
    "Tipo de delito",
    ["Robo", "Asalto", "Vandalismo", "Violencia", "Otro"]
)
fecha = st.date_input("Fecha")

if st.button("Guardar"):

    datos = {
        "tipo_delito": tipo,
        "fecha": str(fecha)
    }

    supabase.table("Delitos").insert(datos).execute()

    st.success("✅ Reporte enviado correctamente")