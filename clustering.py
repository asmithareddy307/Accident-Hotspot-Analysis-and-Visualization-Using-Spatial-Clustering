import numpy as np
from sklearn.cluster import DBSCAN

def perform_clustering(data, eps=1.0, min_samples=3):
    coordinates = data[["latitude", "longitude"]].values
    coordinates_radians = np.radians(coordinates)
    earth_radius_km = 6371.0
    dbscan = DBSCAN(
        eps=eps / earth_radius_km,
        min_samples=min_samples,
        metric="haversine"
    )
    clusters = dbscan.fit_predict(coordinates_radians)
    result = data.copy()
    result["cluster"] = clusters
    return result
