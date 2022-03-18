rgb=$1
output=$2

echo -e "import bpy\nfrom mathutils import *\nfrom math import *\nbpy.data.materials['Material.001'].diffuse_color=Color(($rgb))" > tmp.py && blender -b res/walking-gimp.blend -P tmp.py -o //../image/$output/ -F PNG -x 1 -a
