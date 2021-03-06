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

def set_background(strength):
  world = bpy.context.scene.world
  world.use_nodes = True
  nodes = world.node_tree.nodes
  node = nodes[get_node_index(nodes,'BACKGROUND')]
  node.inputs[0].default_value = [1,1,1,1]
  #node.inputs[0].default_value = [0,0,0,1]
  node.inputs[1].default_value = strength
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

materials = [make_material('Red', [0.46,0.1,0.1,1]), make_material('Blue',
  [0.24,0.41,0.7,1]), make_material('Green', [0.27, 0.8, 0.21, 1]),
  make_material('Yellow', [1.0,0.5,0.0,1]), make_material('White', [1,1,1,1]), make_material('WhiteGray', [0.9,0.9,0.9,1]), make_material('BrightGreen', [0.4,1.0,0.14,1]),
  make_material('WhiteMagenta',[0.8,0.48,1.0,1]), make_material('WhiteYellow',
    [1.0,0.75,0.17,1]), make_material('Orange', [1.0,0.37,0.05,1]),
  make_material('BrightYellowGreen', [0.64,1.0,0.05,1]),
  make_material('LightBlue', [0.32,0.42,1,1]), make_material('BrightYellow',
    [1.0,0.67,0.0,1]), make_material('Magenta', [0.72,0.29,1.0,1]),
  make_material('Cyan', [0.1,1.0,0.6,1]), make_material('WhitePurple',
    [0.67,0.6,1.0,1]), make_material('Black', [0.1,0.1,0.1,1]),
  make_material('Grey', [0.46,0.46,0.46,1]), make_material('DarkOrange',
    [0.845,0.179,0.102,1])] 

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

def set_lamp(world_vec, shadow_size, strength):
  scn = bpy.context.scene
  # Set cycles render engine if not selected
  if not scn.render.engine == 'CYCLES':
    scn.render.engine = 'CYCLES'
  bpy.data.objects["Lamp"].data.type = 'SUN'
  #bpy.data.objects["Lamp"].location = (world_vec[0]*2,-world_vec[1]*2,world_vec[2]*2)
  lamp = bpy.data.lamps['Lamp']
  lamp.shadow_soft_size = shadow_size
  lamp.use_nodes = True
  nodes = lamp.node_tree.nodes
  #print(nodes.keys())
  lamp_node = nodes[get_node_index(nodes,'EMISSION')]
  lamp_node.inputs[1].default_value = strength
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
#            lamp.shape = 'RECTANGLE'
#            lamp.size_y = length2
#            self.__scene.render.engine = 'CYCLES'
#            lamp.cycles.use_multiple_importance_sampling = True
#            lamp.use_nodes = Truerue
#            self.__scene.render.engine = tmp_engine

def set_camera(world_vec, rotation):
  #edit the following after getting a good camera position in blender
  #START
  bpy.data.objects["Camera"].location = (107.4,84.0,61.4)
  bpy.data.objects["Camera"].rotation_euler = rotation
  #END
  #bpy.data.objects["Camera"].location = world_vec
  #bpy.data.objects["Camera"].lock_location = (True, True, True)
  x,y,z = world_vec[0], world_vec[1], world_vec[2]
  #bpy.data.cameras["Camera"].clip_end = 200
  bpy.data.cameras["Camera"].clip_end = max(200, math.sqrt(x*x+y*y+z*z)*2)
  #bpy.ops.view3d.camera_to_view_selected()

def print_planes(world_vec, show_planes, scale):
  len_x = world_vec[0]
  len_y = world_vec[1]
  len_z = world_vec[2]

  bpy.ops.mesh.primitive_plane_add(location=(len_x/2.0+1,len_y/2.0+1.25,1.5), rotation=(0,0,0))
  planeXY = bpy.context.scene.objects.active
  planeXY.name = "PlaneXY"
  planeXY.select = True
  planeXY.active_material = bpy.data.materials['Grey']
  if show_planes[0]:
    bpy.data.objects["PlaneXY"].dimensions = (len_x*scale,len_y*scale,0)

  if show_planes[1]:
    planeYZ = planeXY.copy()
    planeYZ.name = "PlaneYZ"
    planeYZ.location = (1.15,len_y/2+1.25,len_z/2+1.5)
    planeYZ.rotation_euler = (0,1.5708,0)
    planeYZ.data = planeXY.data.copy()
    planeYZ.dimensions = (len_z*scale,len_y*scale,0)
    planeYZ.select = True
    bpy.context.scene.objects.link(planeYZ)

  if show_planes[2]:
    planeXZ = planeXY.copy()
    planeXZ.name = "PlaneXZ"
    planeXZ.location = (len_x/2+1,1.25,len_z/2.0+1.5)
    planeXZ.rotation_euler = (1.5708,0,0)
    planeXZ.data = planeXY.data.copy()
    planeXZ.dimensions = (len_x*scale,len_z*scale,0)
    planeXZ.select = True
    bpy.context.scene.objects.link(planeXZ)

  if show_planes[3]:
    planeXZm = planeXY.copy()
    planeXZm.name = "PlaneXZm"
    planeXZm.location = (len_x/2+1,1.25+len_y,len_z/2.0+1.5)
    planeXZm.rotation_euler = (1.5708,0,0)
    planeXZm.data = planeXY.data.copy()
    planeXZm.dimensions = (len_x*scale,len_z*scale,0)
    planeXZm.select = True
    bpy.context.scene.objects.link(planeXZm)

  if show_planes[4]:
    planeXYm = planeXY.copy()
    planeXYm.name = "PlaneXYm"
    planeXYm.location = (len_x/2.0+1,len_y/2.0+1.25,1.5+len_z)
    planeXYm.rotation_euler = rotation=(0,0,0)
    planeXYm.data = planeXY.data.copy()
    planeXYm.dimensions = (len_x*scale,len_y*scale,0)
    planeXYm.select = True
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
  #set_horizon()
  bpy.context.scene.render.engine = 'CYCLES'
  #bpy.context.scene.render.resolution_percentage = 60

def init_spheres(species_size, species_material_names): 
  delta = 0.01
  size = 0.5
  location = (-10,-10,-10)
  spheres = []
  bpy.ops.object.select_all(action='DESELECT')
  for i in range(species_size):
    bpy.ops.mesh.primitive_uv_sphere_add(size=size)
    spheres.append(bpy.context.scene.objects.active)
    polygons = spheres[i].data.polygons
    for j in polygons:
      j.use_smooth = True
    spheres[i].name = "InitSphere %d" % (i)
    spheres[i].location = location
    spheres[i].select = False
    spheres[i].hide_render = True
    spheres[i].active_material = bpy.data.materials[species_material_names[i]]
    size = size+delta
  return spheres

def print_sphere(location, sphere, mat): 
  ob = sphere.copy()
  ob.name = "Sphere (%d, %d, %d)" % (location[0], location[1], location[2])
  ob.location = location
  ob.data = sphere.data.copy()
  #ob.active_material = mat
  ob.select = False
  ob.hide_render = False
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
  return time, coords

def save(filename):
  bpy.ops.wm.save_as_mainfile(filepath=filename)

def render(filename):
  bpy.data.scenes['Scene'].render.filepath = filename
  bpy.ops.render.render(write_still=True)

def remove_molecules():
  bpy.ops.object.select_all(action='DESELECT')
  bpy.ops.object.select_pattern(pattern="Sphere*")
  bpy.ops.object.delete()

def update_time(time):
  bpy.ops.object.mode_set(mode='EDIT')
  bpy.ops.font.delete()
  if time < 1e-3:
    text = "t = %.2f µs" % (time*1e+6)
  elif time < 1:
    text = "t = %.2f ms" % (time*1e+3)
  elif time < 60:
    text = "t = %.2f s" % (time) 
  elif time < 3600:
    text = "t = %d m %d s" % int(time/60), int(aTime)%60
  else:
    text = "t = %d h %d m %d s" % int(time/3600), int(aTime)%3600/60, int(time)%3600%60
  bpy.ops.font.text_insert(text=text)
  bpy.ops.object.mode_set(mode='OBJECT')

def print_time(time, location, rotation):
  bpy.ops.object.text_add(enter_editmode=True, location=location, rotation=rotation)
  ob = bpy.context.active_object
  ob.active_material = bpy.data.materials['White']

if __name__ == "__main__": 
  lamp_shadow_size = 0.08
  lamp_strength = 1.5
  plane_scale = 5
  background_strength = 0.1
  visible_planes = [1, 1, 1, 0, 0, 0]
  camera_rotation = (62*math.pi/180.0,0*math.pi/180.0,140*math.pi/180.0)
  filename = '/home/satya/wrk/blender/mtcoords.csv'
  species_material_names = ['Red','DarkOrange','DarkOrange','Yellow','Blue',
      'Blue']
  f, world_vec, species_size = init_coord_file(filename)
  set_scene()
  set_background(background_strength)
  set_lamp(world_vec, lamp_shadow_size, lamp_strength)
  spheres = init_spheres(species_size, species_material_names)
  bpy.context.scene.render.resolution_percentage = 100
  bpy.context.scene.cycles.samples = 100
  bpy.data.scenes['Scene'].cycles.device = 'GPU'
  bpy.data.scenes['Scene'].render.tile_x = 512
  bpy.data.scenes['Scene'].render.tile_y = 768
  print_planes(world_vec, visible_planes, plane_scale)
  set_camera(world_vec, camera_rotation)
  set_default_camera_view()
  time = 0
  time_location = (87.85, 15.87, 43.9)
  print_time(time, time_location, camera_rotation)
  for i in range(1000): #number of frames
    for j in range(species_size):
      time, c = load_coords(f)
      if len(c):
        loc = (c[0], c[1], c[2])
        for k in range(0, int(len(c)/3)):
          print_sphere((c[k*3],c[k*3+1],c[k*3+2]), spheres[j], materials[j])
    update_time(time)
    render('/home/satya/wrk/blender/image%04d.png' %i)
    remove_molecules()

  #save('/home/satya/wrk/blender/test.blend')
  #render('/home/satya/wrk/blender/image.png')  

