import streamlit as st
from data_processing import load_data
from clustering import perform_clustering
from visualization import create_map
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Accident Hotspot Analysis",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 Accident Hotspot Analysis")
st.subheader("Spatial Clustering Using DBSCAN")

st.sidebar.header("Clustering Settings")

eps = st.sidebar.slider(
    "Search Radius (km)", 0.1, 5.0, 1.0, 0.1
)

min_samples = st.sidebar.slider(
    "Minimum Accidents", 2, 10, 3, 1
)

file_path = "data/accidents.csv"

try:
    data = load_data(file_path)
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

st.header("📊 Accident Data")
st.dataframe(data, use_container_width=True)

clustered_data = perform_clustering(
    data, eps=eps, min_samples=min_samples
)

total_accidents = len(clustered_data)
number_of_clusters = len(set(clustered_data["cluster"]) - {-1})
noise_points = int(sum(clustered_data["cluster"] == -1))

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Accidents", total_accidents)

with col2:
    st.metric("Accident Hotspots", number_of_clusters)

with col3:
    st.metric("Isolated Accidents", noise_points)

st.header("🗺️ Accident Hotspot Map")

accident_map = create_map(clustered_data)
st_folium(accident_map, width=1200, height=600)

st.header("📍 Hotspot Information")

cluster_data = clustered_data[clustered_data["cluster"] != -1]

if len(cluster_data) > 0:
    hotspot_count = (
        cluster_data.groupby("cluster")
        .size()
        .reset_index(name="accident_count")
        .sort_values("accident_count", ascending=False)
    )
    st.dataframe(hotspot_count, use_container_width=True)
else:
    st.warning(
        "No hotspots found. Try increasing the search radius "
        "or decreasing minimum accidents."
    )

csv = clustered_data.to_csv(index=False)

st.download_button(
    label="⬇️ Download Clustered Data",
    data=csv,
    file_name="accident_hotspot_results.csv",
    mime="text/csv"
)
