from bs4 import BeautifulSoup
import requests

wiki_page_pkmn_name = "Bulbasaur"

#Get the HTML of the bulbapedia page for the pokemon specified in the wiki_page_pkmn_name var
source = requests.get('https://bulbapedia.bulbagarden.net/wiki/' + wiki_page_pkmn_name + '_(Pokémon)').text

list_source = requests.get('https://bulbapedia.bulbagarden.net/wiki/List_of_Pokémon_by_National_Pokédex_number').text

#set the parser
soup = BeautifulSoup(source, 'lxml')

list_soup = BeautifulSoup(list_source, 'lxml')

def get_pkmn_id():
	namref = list_soup.find('a', title=wiki_page_pkmn_name + " (Pokémon)")
	num = (namref.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element)
	return((num[2:5]))

def get_pkmn_name():
	html_name = soup.find('h1', class_='firstHeading').text
	# print(type(html_name))
	name = html_name[:-9]
	
	return(name)

def get_pkmn_types():
	types = []

	for item in soup.find_all('td', width='45px'):
		item.next_element
		print(item)

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

get_pkmn_types()