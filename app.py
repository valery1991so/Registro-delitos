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
st.set_page_config(
    page_title="Registro de Delitos",
    page_icon="🚨",
    layout="centered"
)

st.title("🚨Registro de Delitos")
st.markdown("### Reporta rápidamente lo ocurrido")
st.divider()

st.subheader("¿Qué deseas reportar?")
tipo_delito = None

col1, col2 = st.columns(2)

with col1:
    if st.button("🚗 Robo de vehículo", use_container_width=True):
        tipo_delito = "Robo de vehículo"

    if st.button("📱 Robo de celular", use_container_width=True):
        tipo_delito = "Robo de celular"

    if st.button("🧱 Vandalismo", use_container_width=True):
        tipo_delito = "Vandalismo"

with col2:
    if st.button("⚠️ Asalto", use_container_width=True):
        tipo_delito = "Asalto"

    if st.button("👤 Persona sospechosa", use_container_width=True):
        tipo_delito = "Persona sospechosa"

    if st.button("📍 Otro", use_container_width=True):
        tipo_delito = "Otro"

if tipo_delito:

    st.success(f"Seleccionaste: {tipo_delito}")

    fecha = st.date_input("📅 Fecha del incidente")

    latitud = st.text_input("🌍 Latitud")
    longitud = st.text_input("🌎 Longitud")

    

    if st.button("✅ Enviar reporte", use_container_width=True):

        datos = {
            "tipo": tipo_delito,
            "fecha": str(fecha),
            "latitud": latitud,
            "longitud": longitud
        }

    


supabase.table("Delitos").insert(datos).execute()

st.success("✅ Reporte enviado correctamente")