echo usage render.sh rgb outputfolder [start] [end]
rgb=$1
output=$2
start=$3
end=$4
if [ "$start" == "" ]; then start=1; fi
if [ "$end" == "" ]; then end=10; fi
if [ "$rgb" == "" ]; then exit; fi
if [ "$output" == "" ]; then exit; fi
echo -e "import bpy\nfrom mathutils import *\nfrom math import *\nbpy.data.materials['Material.001'].diffuse_color=Color(($rgb))\nbpy.context.scene.frame_start=$start\nbpy.context.scene.frame_end=$end" > tmp.py && blender -b res/walking-gimp.blend -P tmp.py -o //../image/$output/ -F PNG -x 1 -a
