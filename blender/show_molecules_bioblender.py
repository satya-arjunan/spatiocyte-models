import bpy

def make_material(name, color_diffuse, color_specular, alpha):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = color_diffuse
    mat.diffuse_shader = 'LAMBERT'
    mat.diffuse_intensity = 1.0
    mat.specular_color = color_specular
    mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 0.02
    mat.alpha = alpha
    mat.ambient = 1
    return mat

red = make_material('Red', (0.46,0.1,0.1), (1.0,1.0,1.0), 1)
green = make_material('Green', (0,1,0), (1,1,1), 1)
blue = make_material('Blue', (0,0.3,1), (1,1,1), 1)
white_trans = make_material('White', (1,1,1), (0.2,0.2,0.2), 0.4)
white = make_material('White', (1,1,1), (1,1,1), 1)
black = make_material('Black', (0,0,0), (1,1,1), 1)

def remove_default_cube():
    if "Cube" in bpy.data.objects:
      bpy.data.objects["Cube"].select = True
      bpy.ops.object.delete()

def set_lamp():
    bpy.data.objects["Lamp"].data.type = 'POINT'
    bpy.data.objects["Lamp"].location = (20,20,20)

def set_camera(location=(34,42,24), rotation=(1.08, 0.013, 2.43)):
    bpy.data.objects["Camera"].location = location
    bpy.data.objects["Camera"].rotation_euler = rotation

def set_horizon():
    bpy.context.scene.world.horizon_color = (1,1,1)

def set_scene():
    remove_default_cube()
    #set_lamp()
    #set_camera()
    #set_horizon()
    #bpy.context.scene.render.engine = 'CYCLES'
    #bpy.context.scene.render.resolution_percentage = 60

def print_first_sphere(location): 
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.mesh.primitive_uv_sphere_add(size=1)
    sphere = bpy.context.active_object
    polygons = sphere.data.faces
    for i in polygons:
      i.use_smooth = True
    sphere.name = "Sphere (%d, %d, %d)" % (location[0], location[1],
            location[2])
    sphere.location = location
    sphere.select = False
    sphere.data.materials.append(red)
    return sphere

def print_sphere(location, sphere): 
    ob = sphere.copy()
    ob.name = "Sphere (%d, %d, %d)" % (location[0], location[1], location[2])
    ob.location = location
    ob.data = sphere.data.copy()
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

if __name__ == "__main__": 
  filename = '/home/satya/wrk/blender/mtcoords.csv'
  c = load_coord_file(filename)
  set_scene()
  sphere = print_first_sphere((0,0,0))
  #sphere = print_first_sphere((0,0,0))
  print_sphere((0,0,1), sphere)
  print_sphere((0,1,0), sphere)
  print_sphere((0,1,1), sphere)
  print_sphere((1,0,0), sphere)
  print_sphere((1,0,1), sphere)
  print_sphere((1,1,0), sphere)
  print_sphere((1,1,1), sphere)

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
