from pygal_maps_world.i18n import COUNTRIES
# 由于.json文件中存放的三个字母的国别码，而pygame使用两个字母的国别码
for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])