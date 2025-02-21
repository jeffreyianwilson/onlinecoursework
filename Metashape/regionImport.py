# This python script will import a bounding box region json file into Metashape
# By Jeffrey Ian Wilson for the 3D Scanning Masterclass (www.jeffreyianwilson.com)

import Metashape
import json
import os, sys

# Predefined file paths (Change these as needed)
IMPORT_PATH = str(sys.argv[1])

# Imports the reconstruction region (bounding box) from a CSV file.
def import_reconstruction_region():    
    doc = Metashape.app.document
    chunk = doc.chunk
    if not chunk:
        print("No active chunk found!")
        return
    
    if not os.path.exists(IMPORT_PATH):
        print(f"Error: {IMPORT_PATH} not found!")
        return

    with open(IMPORT_PATH, "r") as f:
        region_data = json.load(f)

    region = chunk.region
    region.center = Metashape.Vector(region_data["center"])
    region.size = Metashape.Vector(region_data["size"])
    
    rotation_matrix = Metashape.Matrix([
        region_data["rotation"][0],
        region_data["rotation"][1],
        region_data["rotation"][2],
    ])
    
    region.rot = rotation_matrix
    chunk.region = region

    print(f"Reconstruction region imported from {IMPORT_PATH}")

# Run function
import_reconstruction_region()
