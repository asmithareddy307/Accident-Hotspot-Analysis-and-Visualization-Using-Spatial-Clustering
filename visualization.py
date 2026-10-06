import folium

def create_map(data):
    center_lat = data["latitude"].mean()
    center_lon = data["longitude"].mean()
    accident_map = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=12
    )
    for _, row in data.iterrows():
        color = "blue" if row["cluster"] == -1 else "red"
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=5,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            popup=f"Cluster: {row['cluster']}"
        ).add_to(accident_map)
    return accident_map
