# 3D Scanning Masterclass
A collection of python scripts for processing data for the 3D Scanning Masterclass.<br>
<hr>
<b>Image Processing/exif2csv.py</b><br>
Python script to parse image exif metadata and compute exposure values into a CSV file then plot the exposure over time in a graph.<br><br>
<b>Image Processing/rtProcessImages.py</b><br>
Python script using Raw Therapee CLI commands to read a raw therapee pp3 file then adjust white balance and adjust exposure to a defined EV value with an exposure offset.<br><br>
<b>Image Processing/addAlpha2image.py</b><br>
This python script will automatically add a directory of image masks then add them as an alpha channel for corresponding imagery.<br><br>
<b>Image Processing/sortImagesIntoFolders.py</b><br>
This python script will automatically sort a directory of images into folders based on the filename prefix.<br>
<hr>
<b>Metashape/alignOptimizeCameras.py</b><br>
This Agisoft Metashape Pro python script will automatically align, filter tie points and optimize cameras.<br><br>
<b>Metashape/importMultiCameraRigMasks.py</b><br>
This Agisoft Metashape Pro python script will automatically import masks on selected images for a multi-camera rig if subdirectory structure is the same.<br><br>
<b>Metashape/adjustReference.py</b><br>
This python script will adjust the pitch, roll, yaw angles defined by user input<br><br>
<b>Metashape/camera2reference.py</b><br>
This python script will create a reference for camera positions file<br><br>
<b>Metashape/optimizeCameras4D.py</b><br>
This python script for Agisoft Metashape Pro will optimize cameras for 4D capture setups.<br>
<hr>
<b>Point Clouds/ply2colmap.py</b><br>
This python script will convert an ascii ply point cloud to a colmap compatible point cloud format.
<hr>
<b>Segmentation/segmentImages.py</b><br>
Python script to detect and mask objects using a trained Yolo segmentation model.<br><br>
