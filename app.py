import streamlit as st
from streamlit_folium import st_folium
import folium
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

    st.markdown("### 📍 Toca el mapa para marcar ubicación")

    mapa = folium.Map(
        location=[14.9006, -92.2634],
        zoom_start=13
    )

    mapa_interactivo = st_folium(
        mapa,
        width=700,
        height=400
    )

    latitud = None
    longitud = None

    if mapa_interactivo["last_clicked"]:

        latitud = mapa_interactivo["last_clicked"]["lat"]
        longitud = mapa_interactivo["last_clicked"]["lng"]

        folium.Marker(
            [latitud, longitud],
            tooltip="Ubicación seleccionada",
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(mapa)

        st.success("📌 Punto marcado correctamente")

    if st.button("✅ Enviar reporte", use_container_width=True):

        if latitud and longitud:

            datos = {
                "tipo_delito": tipo_delito,
                "fecha": str(fecha),
                "latitud": latitud,
                "longitud": longitud
            }

            supabase.table("Delitos").insert(datos).execute()

            st.success("🚨 Reporte enviado correctamente")

        else:
            st.error("Selecciona una ubicación en el mapa")