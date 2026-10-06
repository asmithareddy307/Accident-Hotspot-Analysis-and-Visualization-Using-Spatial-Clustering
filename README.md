# Accident Hotspot Analysis and Visualization Using Spatial Clustering

A beginner-friendly Data Science project using Python, Streamlit and DBSCAN.

## Features
- Accident data loading and cleaning
- DBSCAN spatial clustering
- Accident hotspot identification
- Interactive Folium map
- Dashboard metrics
- Cluster summary
- CSV download

## Requirements
Python 3.11.9 recommended.

## Installation

```bash
py -3.11 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## Dataset

The included `data/accidents.csv` is sample data for testing.
For the final project, replace it with a public road-accident dataset containing
at least `latitude` and `longitude` columns.

## Project Flow

Accident Dataset
-> Data Cleaning
-> Latitude/Longitude
-> DBSCAN
-> Spatial Clustering
-> Hotspot Detection
-> Interactive Map
-> Analysis
