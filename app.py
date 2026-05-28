import streamlit as st
from supabase import create_client
import folium
from streamlit_folium import st_folium

# ---------------- SUPABASE ----------------

url = "TU_URL"
key = "TU_KEY"

supabase = create_client(url, key)

# ---------------- CONFIGURACIÓN ----------------

st.set_page_config(
    page_title="Registro de Delitos",
    page_icon="🚨",
    layout="centered"
)

# ---------------- ESTILO ----------------

st.markdown("""
<style>
.stButton > button {
    width: 100%;
    border-radius: 15px;
    height: 60px;
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TÍTULO ----------------

st.title("🚨 Reporta rápidamente lo ocurrido")

st.write("---")

st.subheader("¿Qué deseas reportar?")

# ---------------- BOTONES ----------------

col1, col2 = st.columns(2)

tipo = None

with col1:
    if st.button("🚗 Robo de vehículo"):
        tipo = "Robo de vehículo"

    if st.button("📱 Robo de celular"):
        tipo = "Robo de celular"

    if st.button("🧱 Vandalismo"):
        tipo = "Vandalismo"

with col2:
    if st.button("⚠️ Asalto"):
        tipo = "Asalto"

    if st.button("📍 Otro"):
        tipo = "Otro"

# Guardar selección
if tipo:
    st.session_state.tipo = tipo

# ---------------- MOSTRAR SELECCIÓN ----------------

if "tipo" in st.session_state:

    st.success(f"Seleccionaste: {st.session_state.tipo}")

    fecha = st.date_input("🗓️ Fecha del incidente")

    st.subheader("📍 Toca el mapa para marcar ubicación")

    # Coordenadas de Tapachula
    mapa = folium.Map(
    location=[14.90, -92.26],
    zoom_start=13,
    tiles="OpenStreetMap"
)

    # Mostrar mapa interactivo
    mapa_data = st_folium(
    mapa,
    width="100%",
    height=450,
    returned_objects=["last_clicked"]
  )

    latitud = None
    longitud = None

    # Detectar clic en mapa
    if mapa_data["last_clicked"] is not None:

        latitud = mapa_data["last_clicked"]["lat"]
        longitud = mapa_data["last_clicked"]["lng"]

        # Mostrar ubicación elegida
        st.success("📌 Ubicación marcada correctamente")

        st.write("Latitud:", latitud)
        st.write("Longitud:", longitud)

    # ---------------- GUARDAR REPORTE ----------------

    if st.button("✅ Enviar reporte"):

        datos = {
            "tipo_delito": st.session_state.tipo,
            "fecha": str(fecha),
            "latitud": latitud,
            "longitud": longitud
        }

        supabase.table("Delitos").insert(datos).execute()

        st.success("🚨 Reporte enviado correctamente")
