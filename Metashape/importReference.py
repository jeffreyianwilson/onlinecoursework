# This python script will import a camera reference csv file into Metashape
# By Jeffrey Ian Wilson for the 3D Scanning Masterclass (www.jeffreyianwilson.com)

import Metashape,sys

doc = Metashape.app.document
chunk = doc.chunk

# Variables
locationAccuracy = float(sys.argv[1])
rotationAccuracy = float(sys.argv[2])
referencePath = str(sys.argv[3]) # "C:\\Temp\\xAngle\\myriam\\reference.csv"

# Import Camera Reference
chunk.importReference(path = referencePath, format = Metashape.ReferenceFormatCSV, skip_rows=2, columns="nxyzabc", delimiter=",")
for camera in chunk.cameras:
    camera.reference.location_accuracy = Metashape.Vector([locationAccuracy,locationAccuracy,locationAccuracy])
    camera.reference.rotation_accuracy = Metashape.Vector([rotationAccuracy,rotationAccuracy,rotationAccuracy])
chunk.updateTransform()
