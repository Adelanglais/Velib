# Velib-and-markets-places

A partir d'une adresse entrée dans le terminale, ce code vous permet de localiser les stations vélibs les plus proches ainsi que les places de marchés.  
API utilisée : 
* géolocalisation <https://api-adresse.data.gouv.fr/search/?q=>
* velib <https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json>
* open data Paris <https://opendata.paris.fr/api/records/1.0/search/?dataset=marches-decouverts&q=&facet=produit&facet=ardt&facet=jours_tenue&facet=lundi&facet=mardi&facet=mercredi&facet=jeudi&facet=vendredi&facet=samedi&facet=dimanche&facet=secteur&facet=gestionnaire>

Format :  JSON

## Installation
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
# Usage

```python
python3 new.py # retourne les coordonnée des stations velib et place de marché les plus proches
```
# Quit virtualenv 
```bash
deactivate
```
