# This python script for Agisoft Metashape Pro will optimize cameras for 4D capture setups
# By Jeffrey Ian Wilson for the 3D Scanning Masterclass (www.jeffreyianwilson.com)

import Metashape
import sys

doc = Metashape.app.document
chunk = doc.chunk
    
# Optimize 4D Cameras Variables
reprojectionError = float(sys.argv[1])
reconstructionUncertainty = float(sys.argv[2])
imageCount = int(sys.argv[3])
projectionAccuracy = float(sys.argv[4])
f = Metashape.TiePoints.Filter()

# Gradual Selection and Optimization for All Frames
if chunk.frames:
    for frame in chunk.frames:
        chunk.frame = frame
        f.init(chunk, criterion=Metashape.TiePoints.Filter.ReprojectionError)
        f.removePoints(reprojectionError)
        chunk.optimizeCameras()

    for frame in chunk.frames:
        chunk.frame = frame
        f.init(chunk, criterion=Metashape.TiePoints.Filter.ReconstructionUncertainty)
        f.removePoints(reconstructionUncertainty)
        chunk.optimizeCameras()

    for frame in chunk.frames:
        f.init(chunk, criterion = Metashape.TiePoints.Filter.ImageCount)
        f.removePoints(imageCount)
        chunk.optimizeCameras()

    for frame in chunk.frames:
        chunk.frame = frame
        f.init(chunk, criterion=Metashape.TiePoints.Filter.ProjectionAccuracy)
        f.removePoints(projectionAccuracy)
        chunk.optimizeCameras()

    for frame in chunk.frames:
        chunk.frame = frame
        f.init(chunk, criterion=Metashape.TiePoints.Filter.ReprojectionError)
        f.removePoints(reprojectionError)
        chunk.optimizeCameras()