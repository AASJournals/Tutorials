#
# This is run in the following way -
#    visit -nowin -cli -s example.py
#

from math import cos, sin, sqrt

database = "localhost:/Applications/VisIt.app/Contents/Resources/data/noise.silo"
#
# This is going to use a single node for visualization.
# For large models, one would use parallel nodes across a cluster.
#
OpenDatabase(database, 0)

# contour plot of a variable
AddPlot("Contour", "hardyglobal", 1, 1)
DrawPlots()

# Modify Annotations!
#
#    Use bold fonts.
#    Turn off user information.
#    Turn off database information.

AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes3D.xAxis.title.font.bold = 1
AnnotationAtts.axes3D.xAxis.label.font.bold = 1
AnnotationAtts.axes3D.yAxis.title.font.bold = 1
AnnotationAtts.axes3D.yAxis.label.font.bold = 1
AnnotationAtts.axes3D.zAxis.title.font.bold = 1
AnnotationAtts.axes3D.zAxis.label.font.bold = 1

AnnotationAtts.userInfoFlag = 0
AnnotationAtts.databaseInfoFlag = 0

AnnotationAtts.axesArray.axes.title.font.bold = 1
AnnotationAtts.axesArray.axes.label.font.bold = 1

SetAnnotationAttributes(AnnotationAtts)

# Modify Rendering!
#
#   Use antialiasing ( can help with text ).

RenderingAtts = RenderingAttributes()
RenderingAtts.antialiasing = 1
SetRenderingAttributes(RenderingAtts)

# Generate the Frames!
#   
#   Many ways to do this but in this case - change the view normal.
#   24 frames in 360 degree rotation
#   13 lanes of tilt ( 180 degrees 
#   html has lane 6 as the zero tilt plane
#
#   This does not have to conform to equal angles.

for lane in range ( 0, 13 ) :
   for frame in range ( 0, 24 ) :

      image = "noise_%02d_%02d" % ( lane, frame )

      rot = float( frame ) * 15.0 * 3.14159 / 180.0
      vx  = cos( rot )
      # vy is tilt since viewUp is on y axis
      vy  = 0.95 - ( 0.95 / 6.0 ) * float( lane )
      vz  = sin( rot )
      s   = sqrt( ( 1.0 - ( vy * vy ) ) / ( vx * vx + vz * vz ) )
      vx  = vx * s
      vz  = vz * s

      View3DAtts = View3DAttributes()
      View3DAtts.viewNormal = ( vx, vy, vz )
      View3DAtts.focus = (0, 0, 0)
      View3DAtts.viewUp = (0.0, 1.0, 0.0 )
      View3DAtts.viewAngle = 30
      View3DAtts.parallelScale = 17.3205
      View3DAtts.nearPlane = -34.641
      View3DAtts.farPlane = 34.641
      View3DAtts.imagePan = (0, 0)
# zoom out 
      View3DAtts.imageZoom = 0.7
      SetView3D(View3DAtts)

      DrawPlots()

# Save images!
#    jpeg (512x512)

      SaveWindowAtts = SaveWindowAttributes()
      SaveWindowAtts.outputToCurrentDirectory = 1
      SaveWindowAtts.outputDirectory = "."
      SaveWindowAtts.fileName = image
      SaveWindowAtts.family = 0
      SaveWindowAtts.format = SaveWindowAtts.JPEG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
      SaveWindowAtts.width = 512
      SaveWindowAtts.height = 512
      SaveWindowAtts.quality = 75
      SetSaveWindowAttributes(SaveWindowAtts)

      SaveWindow()

DeleteAllPlots( )
CloseDatabase( database )

