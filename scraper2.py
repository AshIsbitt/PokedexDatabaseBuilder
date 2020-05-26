# With thanks to null-sleep for his prior project - https://github.com/null-sleep/Web-Scraper-for-Bulbapedia/blob/master/python-scraper/Scraper.py

from bs4 import BeautifulSoup as bs
import requests

wiki_home_page = "http://bulbapedia.bulbagarden.net"
pokedex_list_page = wiki_home_page + "/wiki/List_of_Pokémon_by_National_Pokédex_number"


# Takes every link on the pokedex_list_page, parses them using the LXML parser into a .txt file
# then adds every link text to a list and returns said list
def getPokemonUrls():
	pkmn_link_list = []

	listOfUrls = requests.get(pokedex_list_page)
	soup = bs(listOfUrls.text, "lxml")

	for a in soup.select('table[align="center"] td a[title*="Pok"]'):
		pkmn_link_list.append(a.attrs.get('href'))

	return pkmn_link_list
