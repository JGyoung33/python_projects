from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])

def get_country_code(country_name):
    """根据指定的国家，返回pygal使用的国家的国别码"""
    for code,name in COUNTRIES.items():
        if country_name == name:
            return code
    return None

print(get_country_code('Andorra'))
