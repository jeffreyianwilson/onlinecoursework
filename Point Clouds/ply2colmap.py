# This python script will convert an ascii ply point cloud to a colmap compatible point cloud format
# By Jeffrey Ian Wilson for the 3D Scanning Masterclass (www.jeffreyianwilson.com)

import sys
import numpy as np

# Reads an ASCII PLY file and extracts the point cloud data.
def read_ply_ascii(file_path):
    with open(file_path, 'r') as file:
        header = []
        while True:
            line = file.readline().strip()
            header.append(line)
            if line == "end_header":
                break

        # Parse header for format and property info
        has_color = False
        for line in header:
            if "property uchar" in line:
                has_color = True

        # Load points
        data = np.loadtxt(file)
        if has_color:
            return data[:, :6]  # x, y, z, r, g, b
        else:
            return data[:, :3]  # x, y, z

# Writes a COLMAP-compatible points3D.txt file.
def write_colmap_points(points, output_path):
    
    with open(output_path, 'w') as file:
        for i, point in enumerate(points):
            x, y, z = point[:3]
            r, g, b = point[3:] if point.shape[0] > 3 else (0, 0, 0)
            track_id = -1  # No track info available
            file.write(f"{i + 1} {x:.6f} {y:.6f} {z:.6f} {r} {g} {b} {track_id}\n")

# Converts a PLY file to COLMAP points3D.txt format
def convert_ply_to_colmap(ply_path, colmap_path):
    points = read_ply_ascii(ply_path)
    write_colmap_points(points, colmap_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ply2colmap.py pointCloud.ply points3D.txt")
        sys.exit(1)

    ply_path = sys.argv[1]
    colmap_path = sys.argv[2]

    convert_ply_to_colmap(ply_path, colmap_path)
    print(f"Converted {ply_path} to COLMAP format at {colmap_path}")
