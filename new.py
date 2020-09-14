import requests, json
import urllib.parse
import folium
import math

R = 6378000

print('Veuillez renseigner votre adresse au format suivant: numéro, rue, CP ville')
adresse = input()

""" Gestion de l'adresse courante -- Retourne ses coordonnées """
api_geoloc_url = "https://api-adresse.data.gouv.fr/search/?q="
#adresse = "24, boulevard de l'Hôpital, 75005 Paris"
r1 = requests.get(api_geoloc_url + urllib.parse.quote(adresse))  
data_location = json.loads(r1.text) #conversion de l'objet JSON retourné en un dictionnaire python

current_latitude = data_location['features'][0]['geometry']['coordinates'][1]
current_longitude = data_location['features'][0]['geometry']['coordinates'][0]


""" Analyse des coordonnées des emplacements de velib -- Retourne leurs coordonnées """

api_velib_url = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
r2 = requests.get(api_velib_url)
data_velib = json.loads(r2.text)

velib_coordonates = []
#velib_name = []

data_stations = data_velib['data']['stations']

for k in data_stations:
    velib_latitude =(k['lat'])
    velib_longitude =(k['lon'])
    velib_coordonates.append([velib_latitude,velib_longitude])

close_positions = []
 
""" Calcul de la distance entre current_position et velib_coordonates """

for velib_latitude, velib_longitude in velib_coordonates:
    lat_a = (math.pi * current_latitude)/180
    lon_a = (math.pi * current_longitude)/180
    lat_b = (math.pi * velib_latitude)/180
    lon_b = (math.pi * velib_longitude)/180     
    if R*(math.pi/2 - math.asin(math.sin(lat_b) * math.sin(lat_a) + math.cos(lon_b - lon_a)*math.cos(lat_b) * math.cos(lat_a))) <= 300 :
        close_positions.append(velib_latitude)
        close_positions.append(velib_longitude)
        # velibs_name = (k['name'])
        # velib_name.append(velibs_name)
if len(close_positions)!=0:
    print("Coordonnées des vélibs les plus proches: ", close_positions)
    #print("adresse: ", velib_name)
else:
    print("Pas de vélib dans les parrages... Sorry:(")

""" Analyse des coordonnées des emplacements des marchés découverst - Retourne leurs coordonnées """

api_market_url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=marches-decouverts&q=&facet=produit&facet=ardt&facet=jours_tenue&facet=lundi&facet=mardi&facet=mercredi&facet=jeudi&facet=vendredi&facet=samedi&facet=dimanche&facet=secteur&facet=gestionnaire"
r3 = requests.get(api_market_url)
data_market = json.loads(r3.text)

market_coordonates = []
data_market_places = data_market['records']
#market_localisation = []

for k in data_market_places:
    market_latitude =(k['geometry']['coordinates'][1])
    market_longitude =(k['geometry']['coordinates'][0])
    market_coordonates.append([market_latitude,market_longitude])

close_positions_market = []
 
""" Calcul de la distance entre current_position et velib_coordonates """

for market_latitude, market_longitude in market_coordonates:
    lat_a = (math.pi * current_latitude)/180
    lon_a = (math.pi * current_longitude)/180
    lat_b = (math.pi * market_latitude)/180
    lon_b = (math.pi * market_longitude)/180     
    if R*(math.pi/2 - math.asin(math.sin(lat_b) * math.sin(lat_a) + math.cos(lon_b - lon_a)*math.cos(lat_b) * math.cos(lat_a))) <= 1000 :
        close_positions_market.append(market_latitude)
        close_positions_market.append(market_longitude)
        # market_loc = (k['fields']['localisation'])
        # market_localisation.append(market_loc)

if len(close_positions_market)!=0:
    print("Coordonnées des marchés les plus proches: ", close_positions_market)
    #print(market_localisation)
else:
    print("Pas de marchés dans les parrages... Sorry:( ")
 

 