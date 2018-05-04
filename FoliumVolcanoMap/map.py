import folium
import pandas

"""Creates a Map of Volcanoes in USA with Color Markers indicating
Elevation levels"""

data = pandas.read_csv('Volcanoes_USA.txt')
lon = list(data['LON'])
lat = list(data['LAT'])
elev = list(data['ELEV'])

"""Colors for Elevation levels"""
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    if 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[34,-118.24], zoom_start=10, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name='My Map')


"""Adding Circle Markers for each Volcano"""
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius= 6,popup=str(el)+' m',fill=True, fill_color=color_producer(el),color='grey',fill_opacity=0.7))

"""Reads JSON file showing different countries"""
fg.add_child(folium.GeoJson(data=(open('world.json','r', encoding='utf-8-sig').read())))

map.add_child(fg)

"""Creates and Saves the Map in an HTML format """
map.save('Map.html')
