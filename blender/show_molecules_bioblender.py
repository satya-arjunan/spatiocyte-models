import bpy
import random

def make_material(name, color_diffuse, color_specular, alpha):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = color_diffuse
    mat.diffuse_shader = 'LAMBERT'
    mat.diffuse_intensity = 1.0
    mat.specular_color = color_specular
    mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 0.02
    mat.specular_hardness = 20
    mat.use_cubic = True
    mat.alpha = alpha
    mat.ambient = 1
    return mat

#from 2.55/scripts/ui/BioBlender/settings.py
#color={CA:[0.4,1.0,0.14],(0.8,0.48,1.0), S:[1.0,0.75,0.17], P:[1.0,0.37,0.05], MG:[0.64,1.0,0.05], ZN:[0.32,0.42,1], CU:[1.0,0.67,0.0], K:[0.72,0.29,1.0], CL:[0.1,1.0,0.6], MN:[0.67,0.6,1.0]}

materials = [make_material('Red', (0.46,0.1,0.1), (1,1,1), 1), make_material('Black', (0.1,0.1,0.1), (1,1,1), 1),  make_material('Blue', (0.24,0.41,0.7), (1,1,1), 1), make_material('Green', (0.27, 0.8, 0.21), (1,1,1), 1),  make_material('Yellow', (1.0,0.5,0.0), (1,1,1), 1), make_material('White', (0.9,0.9,0.9), (1,1,1), 1)]

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

def print_first_sphere(location, mat): 
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.mesh.primitive_uv_sphere_add(size=0.7)
    sphere = bpy.context.scene.objects.active
    polygons = sphere.data.faces
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

if __name__ == "__main__": 
  filename = '/home/satya/wrk/blender/mtcoords.csv'
  c = load_coord_file(filename)
  set_scene()
  loc = (random.uniform(20, 50), random.uniform(20, 50), random.uniform(50, 80))
  sphere = print_first_sphere(loc, materials[random.randrange(3)])
  for i in range(0,1000):
      l = (random.uniform(20, 50), random.uniform(20, 50), random.uniform(50, 80))
      print_sphere(l, sphere, materials[random.randrange(3)])

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


