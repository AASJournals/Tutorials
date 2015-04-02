# -*- coding: utf-8 -*-
#
# This script demonstrate how to create interactive 3-D models in Python using
# the Mayavi module. 
#
# This script only scratches the surface of what Mayavi can do.
# See the module documentation for more details:
# http://docs.enthought.com/mayavi/mayavi/index.html
#
#
# Created by F. Vogt, January 2015, frederic.vogt@anu.edu.au
#

from mayavi import mlab

# Let's make a green dice ... 
# First, define the dice elements
xs = [0]
ys = [0]
zs = [0]
px = [0,
    -0.25,-0.25,-0.25,0.25, 0.25,0.25,
    -0.5, -0.5,-0.5, -0.5,-0.5,
     0.5, 0.5,
     0,-0.25,0.25,
    -0.25, -0.25, 0.25, 0.25]
py = [0, 
    -0.25, 0, 0.25,-0.25, 0, 0.25,
    0,-0.25,0.25, -0.25, 0.25,
    -0.25,0.25,
    -0.5, -0.5, -0.5, 
    0.5, 0.5, 0.5, 0.5]
pz = [-0.5,
    0.5,0.5, 0.5, 0.5, 0.5,0.5,
    0, -0.25, -0.25, 0.25, 0.25,
    0.25, -0.25,
    0,-0.25, 0.25,
    -0.25,0.25, -0.25, 0.25]
pc = [0,
    6,6,6,6,6,6,
    5,5,5,5,5,
    2,2,
    3,3,3,
    4,4,4,4,]        



# Then, create a Mayavi window
mlab.close(1)
mlab.figure(1,size=(1000,500))

# Add the cube
mlab.points3d(xs,ys,zs, scale_factor=1,scale_mode='none', color=(0,0.7,0),
                mode='cube')

# A dark outline for the look
mlab.outline(color=(0,0,0),line_width = 2.0)

# The different counts on each face
mlab.points3d(px,py,pz,pc, scale_factor=0.2, scale_mode="none", 
                color=(1,1,1),mode='sphere')

# Export the model to WRL
#mlab.savefig('green_dice.wrl')
mlab.savefig('green_dice.x3d')

# And finally, display the dice 
mlab.show()

# Alternatively, we can plot a slightly more complicated 'red dice' with
# transparency, text and a colorbar
# Simply uncomment the lines below and run the code again to generate it.
'''
# Create a mayavi window
mlab.close(2)
mlab.figure(2,size=(1000,700))

# Add some inner spheres with transparency and the cube
mlab.points3d(xs,ys,zs, scale_factor=0.25,color=(1,0.5,0), mode= 'sphere',
                opacity=1)
mlab.points3d(xs,ys,zs, scale_factor=0.5,color=(1,1,1), mode= 'sphere', 
                opacity=0.5)
mlab.points3d(xs,ys,zs, scale_factor=1,scale_mode='none', color=(0.7,0,0),
                mode='cube', opacity=0.5)

# A dark outline for the look
mlab.outline(color=(0,0,0),line_width = 2.0)

# The different cube faces this time with some colors
mlab.points3d(px,py,pz, pc, scale_factor=0.2, scale_mode='none', 
                colormap="bone",mode='sphere')

# And the associated colorbar
mlab.colorbar(orientation="vertical",nb_labels=7)

# Finally add some text
mlab.text(0,0,"This is a dice",z=1)

# Export the model to X3D and WRL
mlab.savefig('./red_dice.x3d')

mlab.show()
'''


