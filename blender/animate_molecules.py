import bpy
import random
import math

def get_node_index(nodes, data_type):
  idx = 0
  for m in nodes:
    if (m.type == data_type):
      return idx
    idx = idx + 1
  return 1

def set_background():
  world = bpy.context.scene.world
  world.use_nodes = True
  nodes = world.node_tree.nodes
  node = nodes[get_node_index(nodes,'BACKGROUND')]
  node.inputs[0].default_value = [1,1,1,1]
  #node.inputs[0].default_value = [0,0,0,1]
  node.inputs[1].default_value = 0.4
  #print(nodes.keys())
  outN = nodes['Background'].outputs[0]
  inN = nodes['World Output'].inputs[0]
  world.node_tree.links.new(outN, inN)

def make_material(mat_name, color):
  scn = bpy.context.scene
  # Set cycles render engine if not selected
  if not scn.render.engine == 'CYCLES':
    scn.render.engine = 'CYCLES'

  mat = bpy.data.materials.new(mat_name)
  mat.use_nodes = True
  nodes = mat.node_tree.nodes

  node = nodes[get_node_index(nodes,'BSDF_DIFFUSE')]
  node.name = 'Diffuse BSDF'
  node.label = 'Diffuse BSDF'
  node.inputs[0].default_value = color

  outN = nodes['Diffuse BSDF'].outputs[0]
  inN = nodes['Material Output'].inputs[0]
  mat.node_tree.links.new(outN, inN)
  return mat

#from 2.55/scripts/ui/BioBlender/settings.py
#color={CA:[0.4,1.0,0.14],(0.8,0.48,1.0), S:[1.0,0.75,0.17], P:[1.0,0.37,0.05], MG:[0.64,1.0,0.05], ZN:[0.32,0.42,1], CU:[1.0,0.67,0.0], K:[0.72,0.29,1.0], CL:[0.1,1.0,0.6], MN:[0.67,0.6,1.0]}

materials = [make_material('Red', [0.46,0.1,0.1,1]), make_material('Black', [0.1,0.1,0.1,1]),  make_material('Blue', [0.24,0.41,0.7,1]), make_material('Green', [0.27, 0.8, 0.21, 1]),  make_material('Yellow', [1.0,0.5,0.0,1]), make_material('White', [0.9,0.9,0.9,1]), make_material('CA', [0.4,1.0,0.14,1]), make_material('un',[0.8,0.48,1.0,1]), make_material('S', [1.0,0.75,0.17,1]), make_material('P', [1.0,0.37,0.05,1]), make_material('MG', [0.64,1.0,0.05,1]), make_material('ZN', [0.32,0.42,1,1]), make_material('CU', [1.0,0.67,0.0,1]), make_material('K', [0.72,0.29,1.0,1]), make_material('CL', [0.1,1.0,0.6,1]), make_material('MN', [0.67,0.6,1.0,1]), make_material('Grey', [0.46,0.46,0.46,1])]

def make_material_cycles():
  scn = bpy.context.scene
  # Set cycles render engine if not selected
  if not scn.render.engine == 'CYCLES':
    scn.render.engine = 'CYCLES'

  mat_name = 'MixedSurfaceMaterial'
  mat = bpy.data.materials.new(mat_name)
  mat.use_nodes = True
  nodes = mat.node_tree.nodes

  node = nodes.new('ShaderNodeBsdfGlossy')
  node.name = 'Glossy_0'
  node.inputs[0].default_value = [0.8, 0.8, 0.8, 1]
  node.inputs[1].default_value = 0.2
  node.location = 10, 220

  node = nodes['Diffuse BSDF']
  node.inputs[0].default_value = [0.009, 0, 0.8, 1]
  node.inputs[1].default_value = 0
  node.location = 10, 60

  node = nodes.new('ShaderNodeMixShader')
  node.name = 'Mix_0'
  node.inputs[0].default_value = 0.5
  node.location = 210, 60

  node = nodes['Material Output']
  node.location = 410, 60

  # Connect nodes
  outN = nodes['Glossy_0'].outputs[0]
  inN = nodes['Mix_0'].inputs[1]
  mat.node_tree.links.new(outN, inN)

  outN = nodes['Diffuse BSDF'].outputs[0]
  inN = nodes['Mix_0'].inputs[2]
  mat.node_tree.links.new(outN, inN)

  outN = nodes['Mix_0'].outputs[0]
  inN = nodes['Material Output'].inputs[0]
  mat.node_tree.links.new(outN, inN)

  return mat

#http://www.blender.org/api/blender_python_api_2_70_5/bpy.types.html
#https://github.com/Antonioya/blender/blob/master/archimesh/src/tools.py
#bpy.data.objects["Icosphere.003"].data.materials
#import bpy
#matName = 'planeGlass'
#bpy.ops.mesh.primitive_plane_add()
#bpy.data.materials.new(matName)
#bpy.data.materials[matName].use_nodes = True
#bpy.data.materials[matName].node_tree.nodes.new(type='ShaderNodeBsdfGlass')
#inp = bpy.data.materials[matName].node_tree.nodes['Material Output'].inputs['Surface']
#outp = bpy.data.materials[matName].node_tree.nodes['Glass BSDF'].outputs['BSDF']
#bpy.data.materials[matName].node_tree.links.new(inp,outp)
#bpy.data.objects['Plane'].active_material = bpy.data.materials[matName]

#bpy.data.objects["Icosphere.003"].active_material.node_tree.nodes["Mix Shader"].inputs["Fac"].default_value
#just hover over the input box to get the corresponding python property

#bpy.data.objects["Icosphere.003"].active_material.node_tree.nodes["Subsurface Scattering"].inputs[0].default_value

#red = make_material('Red', (0.46,0.1,0.1), (1.0,1.0,1.0), 1)
#green = make_material('Green', (0,1,0), (1,1,1), 1)
#blue = make_material('Blue', (0,0.3,1), (1,1,1), 1)
#white_trans = make_material('White', (1,1,1), (0.2,0.2,0.2), 0.4)
#white = make_material('White', (1,1,1), (1,1,1), 1)
#black = make_material('Black', (0,0,0), (1,1,1), 1)

def remove_default_cube():
  if "Cube" in bpy.data.objects:
    bpy.data.objects["Cube"].select = True
    bpy.ops.object.delete()

def set_lamp(world_vec):
  scn = bpy.context.scene
  # Set cycles render engine if not selected
  if not scn.render.engine == 'CYCLES':
    scn.render.engine = 'CYCLES'
  bpy.data.objects["Lamp"].data.type = 'SUN'
  #bpy.data.objects["Lamp"].location = (world_vec[0]*2,-world_vec[1]*2,world_vec[2]*2)
  lamp = bpy.data.lamps['Lamp']
  lamp.use_nodes = True
  nodes = lamp.node_tree.nodes
  #print(nodes.keys())
  lamp_node = nodes[get_node_index(nodes,'EMISSION')]
  #lamp_node.inputs[1].default_value = 5 #Strength
  #lamp_node.inputs[1].default_value = 2 #Strength
  lamp_node.inputs[1].default_value = 1 #Strength
  outN = lamp_node.outputs[0]
  inN = nodes['Lamp Output'].inputs[0]
  lamp.node_tree.links.new(outN, inN)


# name = "AreaLamp.table"
#        lamp = self.__data.lamps.get(name)
#
#        if not lamp:
#            lamp = self.__data.lamps.new(name, 'AREA')
#            tmp_engine = self.__scene.render.engine
#            self.__scene.render.engine = 'BLENDER_RENDER'
#            lamp.shadow_method = 'RAY_SHADOW'
#            lamp.shadow_ray_samples_x = 10
#            lamp.shadow_ray_samples_y = 10
#            lamp.distance = 500.0
#            lamp.energy = 1.0
#            lamp.use_specular = False
#            lamp.size = width2
#            lamp.shape = 'RECTANGLE'
#            lamp.size_y = length2
#            self.__scene.render.engine = 'CYCLES'
#            lamp.cycles.use_multiple_importance_sampling = True
#            lamp.use_nodes = Truerue
#            self.__scene.render.engine = tmp_engine

def set_camera(world_vec):
  #edit the following after placing camera position in blender
  #START
  bpy.data.objects["Camera"].location = (72.13,54.06,160.79)
  bpy.data.objects["Camera"].rotation_euler = (144*math.pi/180.0,math.pi,90*math.pi/180.0)
  #END
  #bpy.data.objects["Camera"].location = world_vec
  #bpy.data.objects["Camera"].lock_location = (True, True, True)
  x,y,z = world_vec[0], world_vec[1], world_vec[2]
  #bpy.data.cameras["Camera"].clip_end = 200
  bpy.data.cameras["Camera"].clip_end = max(200, math.sqrt(x*x+y*y+z*z)*2)
  #bpy.ops.view3d.camera_to_view_selected()

def print_planes(world_vec):
  len_x = world_vec[0]
  len_y = world_vec[1]
  len_z = world_vec[2]
  print(len_x,len_y,len_z)
  mat = materials[16]

  bpy.ops.mesh.primitive_plane_add(location=(len_x/2.0+1,len_y/2.0+1.25,1.5), rotation=(0,0,0))
  planeXY = bpy.context.scene.objects.active
  planeXY.name = "PlaneXY"
  planeXY.select = False
  planeXY.active_material = mat
  bpy.data.objects["PlaneXY"].dimensions = (len_x,len_y,0)

  planeYZ = planeXY.copy()
  planeYZ.name = "PlaneYZ"
  planeYZ.location = (1.15,len_y/2+1.25,len_z/2+1.5)
  planeYZ.rotation_euler = (0,1.5708,0)
  planeYZ.data = planeXY.data.copy()
  planeYZ.dimensions = (len_z,len_y,0)
  planeYZ.select = False
  bpy.context.scene.objects.link(planeYZ)

  planeXZ = planeXY.copy()
  planeXZ.name = "PlaneXZ"
  planeXZ.location = (len_x/2+1,1.25,len_z/2.0+1.5)
  planeXZ.rotation_euler = (1.5708,0,0)
  planeXZ.data = planeXY.data.copy()
  planeXZ.dimensions = (len_x,len_z,0)
  planeXZ.select = False
  bpy.context.scene.objects.link(planeXZ)

  planeXZm = planeXY.copy()
  planeXZm.name = "PlaneXZm"
  planeXZm.location = (len_x/2+1,1.25+len_y,len_z/2.0+1.5)
  planeXZm.rotation_euler = (1.5708,0,0)
  planeXZm.data = planeXY.data.copy()
  planeXZm.dimensions = (len_x,len_z,0)
  planeXZm.select = False
  bpy.context.scene.objects.link(planeXZm)

  planeXYm = planeXY.copy()
  planeXYm.name = "PlaneXYm"
  planeXYm.location = (len_x/2.0+1,len_y/2.0+1.25,1.5+len_z)
  planeXYm.rotation_euler = rotation=(0,0,0)
  planeXYm.data = planeXY.data.copy()
  planeXYm.dimensions = (len_x,len_y,0)
  planeXYm.select = False
  bpy.context.scene.objects.link(planeXYm)

def set_horizon():
  bpy.context.scene.world.horizon_color = (1,1,1)

def set_default_camera_view():
  for scrn in bpy.data.screens:
    if scrn.name == 'Default':
      bpy.context.window.screen = scrn
      for area in scrn.areas:
        if area.type == 'VIEW_3D':
          for space in area.spaces:
            if space.type == 'VIEW_3D':
              space.viewport_shade = 'MATERIAL'
              reg = space.region_3d
              reg.view_perspective = 'CAMERA'
      break
  return

def set_scene():
  remove_default_cube()
  set_background()
  #set_horizon()
  bpy.context.scene.render.engine = 'CYCLES'
  bpy.context.scene.cycles.samples = 100
  #bpy.context.scene.render.resolution_percentage = 60

def print_first_sphere(location, mat): 
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.mesh.primitive_uv_sphere_add(size=0.5)
    sphere = bpy.context.scene.objects.active
    polygons = sphere.data.polygons
    for i in polygons:
      i.use_smooth = True
    sphere.name = "First Sphere (%d, %d, %d)" % (location[0], location[1],
            location[2])
    sphere.location = location
    sphere.select = True
    sphere.active_material = mat
    return sphere

def print_sphere(location, sphere, mat): 
    ob = sphere.copy()
    ob.name = "Sphere (%d, %d, %d)" % (location[0], location[1], location[2])
    ob.location = location
    ob.data = sphere.data.copy()
    ob.active_material = mat
    ob.select = True
    bpy.context.scene.objects.link(ob)
    return ob

def init_coord_file(filename):
  f = open(filename, 'r')
  titles = f.readline().strip().split(',')
  log_interval = float(titles[0].split('=')[1])
  world_vec = [float(titles[1].split('=')[1]), float(titles[2].split('=')[1]),
      float(titles[3].split('=')[1])]
  species_names = []
  species_radii = []
  for i in range(len(titles)-5):
    species_names.append(titles[i+5].split("=")[0])
    species_radii.append(float(titles[i+5].split("=")[1]))
  species_size = len(species_names)
  return f, world_vec, species_size

def load_coords(f):
  coords_str = f.readline().strip().split(",")
  time = float(coords_str[0]) 
  coords = []
  for i in range(len(coords_str)-1):
    coords.append(float(coords_str[i+1]))
  return coords

def save(filename):
  bpy.ops.wm.save_as_mainfile(filepath=filename)

def render(filename):
  bpy.data.scenes['Scene'].render.filepath = filename
  bpy.ops.render.render( write_still=True )

def remove_molecules():
  bpy.ops.object.select_all(action='DESELECT')
  bpy.ops.object.select_pattern(pattern="Sphere*")
  bpy.ops.object.delete()

if __name__ == "__main__": 
  filename = '/home/satya/wrk/blender/CoordinateLog.csv'
  #filename = '/home/satya/wrk/blender/mtcoords.csv'
  f, world_vec, species_size = init_coord_file(filename)
  set_scene()
  set_lamp(world_vec)
  print_planes(world_vec)
  sphere = print_first_sphere((-10,-10,-10), materials[0])
  set_camera(world_vec)
  set_default_camera_view()
  for i in range(2): #number of frames
    for j in range(species_size):
      c = load_coords(f)
      if len(c):
        loc = (c[0], c[1], c[2])
        for k in range(1, int(len(c)/3)):
          print_sphere((c[k*3],c[k*3+1],c[k*3+2]), sphere, materials[j])
    render('/home/satya/wrk/blender/image%d.png' %i)
    remove_molecules()

  #save('/home/satya/wrk/blender/test.blend')
  #render('/home/satya/wrk/blender/image.png')  

