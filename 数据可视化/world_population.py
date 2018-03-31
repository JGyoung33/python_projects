import json
from pygal_maps_world.i18n import COUNTRIES
from pygal.style import LightColorizedStyle as LCS
from country_codes import get_country_code
import pygal
from pygal.style import RotateStyle as RS

#将数据加载到一个列表中
filename = "population_data.json"
with open (filename) as f:
    pop_data = json.load(f)

cc_pop1,cc_pop2,cc_pop3 ={},{},{}
for pop_dict in pop_data:
    if pop_dict["Year"] == '2010':
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code:
            if population < 10000000:
                cc_pop1[code] = population
            elif population <1000000000:
                cc_pop2[code] = population
            else:
                cc_pop3[code] =population
        else:
            print("Error ->" +country_name)

wm_style = RS('#336699',base_style=LCS)
wm = pygal.maps.world.World(style =wm_style)
wm.title=('Populations in world')
wm.add('0-10m',cc_pop1)
wm.add('10m-1bn',cc_pop2)
wm.add('>1bn',cc_pop3)
wm.render_to_file('world_population.svg')
print(len(cc_pop1),len(cc_pop2),len(cc_pop3))



