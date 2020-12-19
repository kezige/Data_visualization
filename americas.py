import pygal_maps_world.maps

# 制作能够测试美洲地区的地图，分为北美，中美，南美，用不同的颜色加以表示
wm=pygal_maps_world.maps.World()
wm.title='North,Central,and South Ametrica'

wm.add('North America',['ca','mx','us'])
wm.add('Central America',['bz','cr','gt','hn','pa','sv'])
wm.add('South America',['ar','bo','br','cl','co','ec','gf',
                        'gy','pe','py','sr','uy','ve'])

wm.render_to_file('americas.svg')