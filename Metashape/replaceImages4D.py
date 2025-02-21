# This python script will replace images for 4D volume capture processing
# By Jeffrey Ian Wilson for the 3D Scanning Masterclass (www.jeffreyianwilson.com)

import Metashape
import os
import sys

def replace_jpg_with_png_in_timeline():
    if len(sys.argv) < 2:
        print("Usage: script.py <PNG_ROOT_PATH>")
        return
    
    PNG_ROOT_PATH = str(sys.argv[1])  # User-provided root directory for PNG files

    doc = Metashape.app.document
    if not doc or not doc.chunk:
        print("No active document or chunk found.")
        return

    chunk = doc.chunk
    total_updated = 0
    total_frames = len(chunk.frames)

    print(f"Processing {total_frames} frames in the timeline...")
    print(f"Looking for PNG images in: {PNG_ROOT_PATH}")

    for frame_index, frame in enumerate(chunk.frames):  # Track frame index manually
        updated_cameras = 0

        for camera in frame.cameras:  # Use frame.cameras instead of treating frame as a chunk
            if not camera.photo:
                continue  # Skip cameras without an assigned photo
            
            old_path = camera.photo.path
            old_dir, filename = os.path.split(old_path)  # Extract folder and filename
            filename_png = os.path.splitext(filename)[0] + ".png"  # Convert to PNG

            # Extract camera folder name (e.g., "cam001")
            cam_folder = os.path.basename(old_dir)  
            
            # Construct the new PNG path using the same structure
            new_path = os.path.join(PNG_ROOT_PATH, cam_folder, filename_png)

            if os.path.exists(new_path):
                camera.photo.path = new_path
                updated_cameras += 1
                print(f"Frame {frame_index}: {old_path} -> {new_path}")
            else:
                print(f"Frame {frame_index}: PNG not found for {old_path}")

        total_updated += updated_cameras
        print(f"Frame {frame_index}: {updated_cameras} cameras updated.")

    print(f"\nTotal cameras updated across all frames: {total_updated}")

# Run the function
replace_jpg_with_png_in_timeline()
