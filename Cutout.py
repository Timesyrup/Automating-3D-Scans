#
# A nurbs path mesh is created before this script is run 
# This script generates a solid shape from the nurbs path mesh
#

import bpy
from mathutils import Vector

#Extrude along the objects normal direction
def extrude_along_direction(obj, distance):

    bpy.ops.object.mode_set(mode='EDIT')
    
    # Check if there are no faces, if so, fill the center
    if not obj.data.polygons:
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.fill()
    
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, distance)})
    bpy.ops.object.mode_set(mode='OBJECT')

# Get the selected object (NURBS path)
selected_object = bpy.context.active_object

# Extrude 10cm in forward direction 
extrude_along_direction(selected_object, 0.1)  
# Extrude 10cm in backward direction
extrude_along_direction(selected_object, -0.1)  


# Then use boolean modification - subtraction to subtract this shape from the cube 
