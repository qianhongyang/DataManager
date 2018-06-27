#coding=utf-8
import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = "世界地图人口分布图"

wm.add('North America',['ca','mx','us'])
wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South America',['ar','bo','br','cl','co','ec','gf','gy','pe','py','sr','uy','ve'])

wm.render_to_file('world.svg')