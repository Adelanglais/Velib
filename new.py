import requests, json
import urllib.parse
import folium

ref_latitude = 0.0008764
ref_longitude = 0.000433

#print('Veuillez renseigner votre adresse au format suivant: numéro, rue, CP ville')
#adresse = input()

""" Gestion de l'adresse courante -- Retourne ses coordonnées """

api_geoloc_url = "https://api-adresse.data.gouv.fr/search/?q="
adresse = "24, boulevard de l'Hopital, 75005 Paris"
r = requests.get(api_geoloc_url + urllib.parse.quote(adresse))
    
data_location = json.loads(r.text) #conversion de l'objet JSON retourné en un dictionnaire python

current_latitude = data_location['features'][0]['geometry']['coordinates'][1]
current_longitude = data_location['features'][0]['geometry']['coordinates'][0]



""" Analyse des coordonnées des emplacements de velib -- Retourne leurs coordonnées """

api_velib_url = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
response = requests.get(api_velib_url)
data_velib = json.loads(response.text)

close_positions = []

for k in range(len(data_velib)):
    velib_latitude = data_velib['data']['stations'][k]['lat']
    velib_longitude = data_velib['data']['stations'][k]['lon']
    
    velib_coordonates = [velib_latitude,velib_longitude] 
    #print (velib_coordonates)

for velib_longitude in velib_coordonates:
    for velib_latitude in velib_coordonates:
        if (current_latitude - velib_latitude <= ref_latitude and current_longitude - velib_longitude <= ref_longitude):
            close_positions.append(velib_coordonates)
if len(close_positions)==0:
    print("Pas de vélib dans les parrages... Sorry:(")
else:
    print ("Coordonnées du vélib le plus proche", close_positions)
    #print(data_velib['data']['stations']['name'])
   








