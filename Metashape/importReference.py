# This python script will import a camera reference csv file into Metashape
# By Jeffrey Ian Wilson for the 3D Scanning Masterclass (www.jeffreyianwilson.com)

import Metashape,sys

doc = Metashape.app.document
chunk = doc.chunk

# Variables
referencePath = str(sys.argv[1]) #"C:\\Temp\\xAngle\\myriam\\reference.csv"

# Import Camera Reference
chunk.importReference(path = referencePath, format = Metashape.ReferenceFormatCSV, skip_rows=2, columns=" nxyz", delimiter=",")
for camera in chunk.cameras:
    camera.reference.location_accuracy = Metashape.Vector([0.01,0.01,0.01])
    #camera.reference.rotation_accuracy = Metashape.Vector([0.1,0.1,0.1])
chunk.updateTransform()