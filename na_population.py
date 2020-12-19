import pygal_maps_world.maps

# 显示三个地区的人口数量
wm=pygal_maps_world.maps.World()
wm.title='Population of Countries in North America'
wm.add('North America',{'ca':34126000,'mx':113423000})

wm.render_to_file('na_population.svg')