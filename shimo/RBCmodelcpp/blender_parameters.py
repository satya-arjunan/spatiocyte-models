#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#
#        This file is part of Spatiocyte particle simulator package
#
#             Copyright (C) 2009-2014 RIKEN, Keio University
#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#
#
# Spatiocyte is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
# 
# Spatiocyte is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public
# License along with Spatiocyte -- see the file COPYING.
# If not, write to the Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# 
#END_HEADER
#
# written by Satya Arjunan <satya.arjunan@gmail.com>
# Spatiocyte, RIKEN Quantitative Biology Center, Osaka, Japan
#

import math

start_frame = 212
end_frame = 213
resolution_x = 1920
resolution_y = 1080
resolution_percentage = 100
render_samples = 50
lamp_shadow_size = 0.1
lamp_strength = 0.5
plane_scale = 5
background_strength = 0.4
visible_planes = [0, 1, 0, 0, 0, 0]
camera_rotation = (136.78*math.pi/180.0, math.pi, 88.8*math.pi/180.0)
camera_location = (54.21, 40.10, 131.41)
time_location = (37.15, 89.48, 125.9)
lamp_location = (7.88, 37.38, 31.51)
lamp_rotation = (-70.36*math.pi/180.0, 42.52*math.pi/180.0, -30.1*math.pi/180.0)
#lamp_location = (4.08, 1.0, 5.9)
#lamp_rotation = (37.26*math.pi/180.0,3.16*math.pi/180.0,106.94*math.pi/180.0)
plane_disp = [1.0, 1.25, 0.0]
#plane_disp = [0.5, 0, 0.5]
#set True if using GPU device to render
GPU_device = True
#for GPU device, set tile_x = 512, tile_y = 512
tile_x = 512
tile_y = 512
plane_material_name = 'White'
time_material_name = 'Black'
filename = 'CoordinateLog.csv'
species_material_names = ['DarkBlue_glossy', 'DarkRed', 'DarkBlue_glossy', 'DarkBlue_glossy','DarkBlue_glossy','DarkBlue_glossy','DarkBlue_glossy','DarkBlue_glossy','DarkBlue_glossy','DarkBlue_glossy', 'Yellow', 'DarkBlue_glossy','DarkBlue_glossy','DarkBlue_glossy','DarkBlue_glossy','DarkBlue_glossy','DarkBlue_glossy','DarkBlue_glossy', 'DarkBlue_glossy']
