import bpy
import random

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
  node.inputs[1].default_value = 0.3
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

materials = [make_material('Red', [0.46,0.1,0.1,1]), make_material('Black', [0.1,0.1,0.1,1]),  make_material('Blue', [0.24,0.41,0.7,1]), make_material('Green', [0.27, 0.8, 0.21, 1]),  make_material('Yellow', [1.0,0.5,0.0,1]), make_material('White', [0.9,0.9,0.9,1])]

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

def set_lamp():
  scn = bpy.context.scene
  # Set cycles render engine if not selected
  if not scn.render.engine == 'CYCLES':
    scn.render.engine = 'CYCLES'
  bpy.data.objects["Lamp"].data.type = 'SUN'
  lamp = bpy.data.lamps['Lamp']
  lamp.use_nodes = True
  nodes = lamp.node_tree.nodes
  #print(nodes.keys())
  lamp_node = nodes[get_node_index(nodes,'EMISSION')]
  lamp_node.inputs[1].default_value = 5 #Strength
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
#            lamp.use_nodes = True
#            self.__scene.render.engine = tmp_engine

def set_camera(location=(34,42,24), rotation=(1.08, 0.013, 2.43)):
  bpy.data.objects["Camera"].location = location
  bpy.data.objects["Camera"].rotation_euler = rotation

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
  set_default_camera_view()
  set_background()
  set_lamp()
  #set_camera()
  #set_horizon()
  bpy.context.scene.render.engine = 'CYCLES'
  bpy.context.scene.cycles.samples = 100
  #bpy.context.scene.render.resolution_percentage = 60

def print_first_sphere(location, mat): 
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.mesh.primitive_uv_sphere_add(size=0.3)
    sphere = bpy.context.scene.objects.active
    polygons = sphere.data.polygons
    for i in polygons:
      i.use_smooth = True
    sphere.name = "Sphere (%d, %d, %d)" % (location[0], location[1],
            location[2])
    sphere.location = location
    sphere.select = False
    sphere.active_material = mat
    return sphere

def print_sphere(location, sphere, mat): 
    ob = sphere.copy()
    ob.name = "Sphere (%d, %d, %d)" % (location[0], location[1], location[2])
    ob.location = location
    ob.data = sphere.data.copy()
    ob.active_material = mat
    bpy.context.scene.objects.link(ob)
    return ob

def load_coord_file(filename):
  f = open(filename, 'r')
  titles = f.readline().strip().split(',')
  log_interval = float(titles[0].split('=')[1])
  world_width = float(titles[1].split('=')[1])
  world_height = float(titles[2].split('=')[1])
  world_length = float(titles[3].split('=')[1])
  voxel_radius = float(titles[4].split('=')[1])
  species_names = []
  species_radii = []
  for i in range(len(titles)-5):
    species_names.append(titles[i+5].split("=")[0])
    species_radii.append(float(titles[i+5].split("=")[1]))
  species_size = len(species_names)
  log_cnt = 0
  for line in f:
    coords_str = line.strip().split(",")
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

if __name__ == "__main__": 
  filename = '/home/satya/wrk/blender/mtcoords.csv'
  c = load_coord_file(filename)
  set_scene()
  loc = (random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5))
  sphere = print_first_sphere(loc, materials[random.randrange(6)])
  for i in range(0,1000):
      loc = (random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5))
      print_sphere(loc, sphere, materials[random.randrange(6)])
  save('/home/satya/wrk/blender/test.blend')
  render('/home/satya/wrk/blender/image.png')  

#import bpy
#import math

#def degToRad(angleDeg):
#    return (pi * angleDeg / 180.0)

#def set_sun_position(elevation, azimuth, radius):
#    sd = bpy.data.worlds['World'].node_tree.nodes['Sky Texture'].sun_direction
#    theta = pi / 2 - degToRad(elevation)
#    phi = degToRad(-azimuth)
#    sd.x = sin(phi) * sin(-theta)
#    sd.y = sin(theta) * cos(phi)
#    sd.z = cos(theta)
#    return sd * radius
    
#bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=1.0, location=(10, 0, 0))
#obj = bpy.context.active_object


# Set sun elevation to 30 degrees and azimuth 90 with sun object at
# a distance of 20 blender units from the world center.
#obj.location = set_sun_position(30, 90, 20)
