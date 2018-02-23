import pandas as pd
# INSTRUCCION
# Es necesario instalar el paquete folium desde Anaconda Navigator
import folium

# INSTRUCCION
# Debeis descargaros un fichero csv con un conjunto de registros (records) de una especie
# desde la pagina del OBIS: http://www.iobis.org y leerla en un DataFrame de pandas
# que se llame specie con pd.read_csv
specie1 =pd.read_csv('Aureliaaurita.csv') 
specie2=pd.read_csv('Cothilorizatuberculata.csv')

# Lectura de latitud y longitud de las observaciones
lon1, lat1 = specie1['decimalLongitude'], specie1['decimalLatitude']
lon2, lat2 = specie2 ['decimalLongitude'], specie2['decimalLatitude']

# MODIFICABLE
# Lectura de datos adicionales (se deben convertir a cadena para visualizarlos)
dates1 = specie1['eventDate'].astype('str')
dates2 = specie2['eventDate'].astype('str')

# MODIFICABLE
# Opciones de visualizacion de la especie
# Debeis ajustar las coordenadas y el zoom del mapa a la localizacion de la especie
# Muchas mas en: http://python-visualization.github.io/folium/docs-v0.5.0/modules.html
m = folium.Map(location=[50, 10], zoom_start=3, tiles='Stamen Watercolor')

# Creacion del conjunto de puntos
feature_group = folium.FeatureGroup('Ocurrences')

# MODIFICABLE
for lon1, lat1, dates1 in zip(lon1, lat1, dates1):
    feature_group.add_child(folium.CircleMarker(radius=1,location=[lat1, lon1], popup=dates1, color='#040102', fill_color='#cc3186'))
for lon2, lat2, dates2 in zip(lon2, lat2, dates2):
    feature_group.add_child(folium.RegularPolygonMarker(location=[lat2, lon2], popup=dates2, color='#040102', fill_color='#7bde43', radius=1))
# Se incorporan los puntos al mapa
m.add_child(feature_group)

# Se guarda el mapa como una pagina web
m.save('mapa6.html')
