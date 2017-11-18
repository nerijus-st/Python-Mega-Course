import folium
import pandas

map = folium.Map(location=[36, -115], zoom_start=5, tiles="Mapbox Bright")
data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

fg = folium.FeatureGroup(name="My Map")


def get_volcanoe_color(elev):
    if elev < 2000:
        return "green"
    if elev >= 2000 and elev < 3000:
        return "orange"
    if elev >= 3000 and elev < 3500:
        return "red"
    else:
        return "darkred"

fgp_volcanoes = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lat, lon, elev):
    elev_color = get_volcanoe_color(int(el))
    fgp_volcanoes.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el) + "m", radius=8,
                                                fill_color=elev_color, fill=True, color="white", fill_opacity=0.7))

fgp_population = folium.FeatureGroup(name="Population")
fgp_population.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                                        style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 5000000
                                                                  else 'green' if 5000000 <= x['properties']['POP2005'] < 10000000 else
                                                                  'red' if 10000000 <= x['properties']['POP2005'] < 50000000
                                                                  else 'darkblue' if 50000000 <= x['properties']['POP2005'] < 100000000
                                                                  else 'black'}))

map.add_child(fgp_volcanoes)
map.add_child(fgp_population)
map.add_child(folium.LayerControl())

map.save("Map1.html")
