# This python script will export the Metashape bounding box region to a json file
# By Jeffrey Ian Wilson for the 3D Scanning Masterclass (www.jeffreyianwilson.com)

import Metashape
import json,sys

# Predefined file paths (Change these as needed)
# EXPORT_PATH = "C:\\Temp\\xAngle\\myriam\\region.csv"
EXPORT_PATH = str(sys.argv[1])

# Exports the reconstruction region (bounding box) to a CSV file.
def export_reconstruction_region():    
    doc = Metashape.app.document
    chunk = doc.chunk
    if not chunk:
        print("No active chunk found!")
        return
    
    region = chunk.region
    region_data = {
        "center": [region.center.x, region.center.y, region.center.z],
        "size": [region.size.x, region.size.y, region.size.z],
        "rotation": [
            [region.rot[0, 0], region.rot[0, 1], region.rot[0, 2]],
            [region.rot[1, 0], region.rot[1, 1], region.rot[1, 2]],
            [region.rot[2, 0], region.rot[2, 1], region.rot[2, 2]],
        ],
    }

    with open(EXPORT_PATH, "w") as f:
        json.dump(region_data, f, indent=4)

    print(f"Reconstruction region exported to {EXPORT_PATH}")

# Run both functions automatically
export_reconstruction_region()
