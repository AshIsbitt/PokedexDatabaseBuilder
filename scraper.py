from bs4 import BeautifulSoup
import requests

wiki_page_pkmn_name = "Bulbasaur"

#Get the HTML of the bulbapedia page for the pokemon specified in the wiki_page_pkmn_name var
source = requests.get('https://bulbapedia.bulbagarden.net/wiki/' + wiki_page_pkmn_name + '_(Pokémon)').text

#set the parser
soup = BeautifulSoup(source, 'lxml')

def get_pkmn_id():
	pass

def get_pkmn_name():
	html_name = soup.find('h1', class_='firstHeading').text
	# print(type(html_name))
	name = html_name[:-9]
	
	return(name)

def get_pkmn_types():
	pass

def get_pkmn_height():
	pass

def get_pkmn_weight():
	pass

def get_pkmn_prev_form():
	pass

def get_pkmn_next_form():
	pass

def get_pkmn_evolve_level():
	pass

def get_pkmn_second_evolve_level():
	pass


get_pkmn_id()