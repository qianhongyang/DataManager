#coding=utf-8
import pygal
import pygal_maps_world.maps
import json
from country_codes import  get_country_code

filename = 'population_data.json'

with open(filename) as f:
    pop_data=json.load(f)

cc_populations = {}
for pop_dic in pop_data:
    if pop_dic['Year'] == "2010":
        country_name = pop_dic["Country Name"]
        population = int(float(pop_dic["Value"]))
        # print(country_name + ":" + population)
        code = get_country_code(country_name)
        if code:
            cc_populations[code]=population

cc_pops1,cc_pops2,cc_pops3={},{},{}
for cc,pop in cc_populations.items():
    if pop < 10000000:
        cc_pops1[cc] = pop
    elif pop < 1000000000:
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop

wm = pygal_maps_world.maps.World()
wm.title = "世界人口地图"
# wm.add('2010',cc_populations)
wm.add('0-10m',cc_pops1)
wm.add('10m-1bn',cc_pops2)
wm.add('>1bn',cc_pops3)
wm.render_to_file('world_populations.svg')
