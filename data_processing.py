import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    data = data.dropna(subset=["latitude", "longitude"])
    data["latitude"] = pd.to_numeric(data["latitude"], errors="coerce")
    data["longitude"] = pd.to_numeric(data["longitude"], errors="coerce")
    data = data.dropna(subset=["latitude", "longitude"])
    data = data[
        (data["latitude"] >= -90) & (data["latitude"] <= 90) &
        (data["longitude"] >= -180) & (data["longitude"] <= 180)
    ]
    return data
