# This python script will export LiDAR panorama positions to a reference file
# By Jeffrey Ian Wilson for the 3D Scanning Masterclass (www.jeffreyianwilson.com)

import Metashape
import math

def rotation_matrix_to_ypr(R):
    """ Convert a rotation matrix to yaw, pitch, roll angles in degrees. """
    r00, r01, r02 = R[0,0], R[0,1], R[0,2]
    r10, r11, r12 = R[1,0], R[1,1], R[1,2]
    r20, r21, r22 = R[2,0], R[2,1], R[2,2]

    # Compute angles in degrees
    yaw = math.degrees(math.atan2(r10, r00))
    pitch = math.degrees(-math.asin(r20))
    roll = math.degrees(math.atan2(r21, r22))

    return yaw, pitch, roll

# **Apply systematic rotational offsets based on error pattern analysis**
YAW_OFFSET = -90.0
PITCH_OFFSET = 0.0
ROLL_OFFSET = -90.0

# Get current document and chunk
doc = Metashape.app.document
chunk = doc.chunk

if not chunk.crs:
    print("No coordinate system defined for the chunk. Please set a CRS before running this script.")
    raise SystemExit

for camera in chunk.cameras:
    if not camera.transform:
        continue  # Skip unaligned cameras
    
    # Extract camera position
    camera_center = camera.center
    camera_coord = chunk.crs.project(chunk.transform.matrix.mulp(camera_center))

    # Extract rotation matrix
    R = Metashape.Matrix([[camera.transform[0,0], camera.transform[0,1], camera.transform[0,2]],
                          [camera.transform[1,0], camera.transform[1,1], camera.transform[1,2]],
                          [camera.transform[2,0], camera.transform[2,1], camera.transform[2,2]]])

    # Compute Yaw, Pitch, Roll
    yaw, pitch, roll = rotation_matrix_to_ypr(R)

    # **Apply corrected offsets**
    yaw_corrected = yaw + YAW_OFFSET
    pitch_corrected = pitch + PITCH_OFFSET
    roll_corrected = roll + ROLL_OFFSET

    # **Ensure values stay within -180° to 180° range**
    yaw_corrected = (yaw_corrected + 180) % 360 - 180
    pitch_corrected = (pitch_corrected + 180) % 360 - 180
    roll_corrected = (roll_corrected + 180) % 360 - 180

    # Set camera reference with corrected values
    camera.reference.location = Metashape.Vector(camera_coord)
    camera.reference.rotation = Metashape.Vector([yaw_corrected, pitch_corrected, roll_corrected])
