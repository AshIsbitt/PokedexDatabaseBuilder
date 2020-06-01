# With thanks to null-sleep for his prior project - https://github.com/null-sleep/Web-Scraper-for-Bulbapedia/blob/master/python-scraper/Scraper.py

from bs4 import BeautifulSoup as bs
import requests
import sqlalchemy

wiki_home_page = "http://bulbapedia.bulbagarden.net"
pokedex_list_page = wiki_home_page + "/wiki/List_of_Pokémon_by_National_Pokédex_number"
pkmn_stats = [ 	'id', 
				'name', 
				'type', 
				'abilities', 
				'hp', 
				'attack', 
				'defense', 
				'sp_atk', 
				'sp_def', 
				'speed', 
				'BST', 
				'weight', 
				'height', 
				'prev_form', 
				'next_forms']


# Takes every link on the pokedex_list_page, parses them using the LXML parser into a .txt file
# then adds every link text to a list and returns said list
def getPokemonUrls():
	pkmn_link_list = []

	listOfUrls = requests.get(pokedex_list_page)
	soup = bs(listOfUrls.text, 'html.parser')

	for a in soup.select('table[align="center"] td a[title*="Pok"]'):
		pkmn_link_list.append(a.attrs.get('href'))

	return pkmn_link_list

# for each URL passed into this function, get all the required stats
def getPokemonData(inputUrl):
	pkmn_data = []
	htmldata = requests.get(wiki_home_page + inputUrl)
	soup = bs(htmldata.text, 'html.parser')

	# Pokemon ID
	idnum = str(soup.select('th big a[href*="mon_by_National_Pok"] ')[0])
	idnum = idnum[-14:-11]
	print(idnum)

	pkmn_data.append(idnum)

	#Pokemon name
	pkmn_name = soup.find('h1', class_='firstHeading').text[:-9]
	print(pkmn_name)
	pkmn_data.append(pkmn_name)

	#Pokemon types
	pkmn_types = []

	for x in range(0,2):
		typetext = str(soup.select('a[href*="(type)"] span b')[x])[3:-4]

		if typetext != "Unknown":
			pkmn_types.append(typetext)

	print(pkmn_types)

	pkmn_data.append(pkmn_types)

	#Pokemon Abilities
	pkmn_abilities = []

	for x in range(0, len(soup.select('td a[href*="(Ability)"] span'))):
		abilitytext = str(soup.select('td a[href*="(Ability)"] span')[x])[26:-7]
		
		if abilitytext != "Cacophony":
			pkmn_abilities.append(abilitytext)

	print(pkmn_abilities)
	pkmn_data.append(pkmn_abilities)

	#Base Stats
	#print((soup.select('table[style="background\\: #78C850"] tbody tr[style*="background\\: "] th[style*="width\\:85px"] div[style="float\\:right"]')[1]))

	trs = soup.find_all("table", {'style': "table[style=\"background\\: #78C850\"] tbody tr[style*=\"background\\: \"] th[style*=\"width\\:85px\"] div[style=\"float\\:right\"]"})

	for tr in trs:
 		print(tr["style"])


	# pkmn_data.append((soup.select('td table[cellspacing="0"] tr th')[1].get_text()))
	# pkmn_data.append((soup.select('td table[cellspacing="0"] tr th')[3].get_text()))
	# pkmn_data.append((soup.select('td table[cellspacing="0"] tr th')[5].get_text()))
	# pkmn_data.append((soup.select('td table[cellspacing="0"] tr th')[7].get_text()))
	# pkmn_data.append((soup.select('td table[cellspacing="0"] tr th')[9].get_text()))
	# pkmn_data.append((soup.select('td table[cellspacing="0"] tr th')[11].get_text()))
	# pkmn_data.append((soup.select('td table[cellspacing="0"] tr th')[13].get_text()))

	#Weight
	weight_stat = soup.select('table.roundy tr td.roundy b a[href*="weight"]')[ 0 ].parent.parent
	weight = (float(((weight_stat.select( 'table tr td' )[ 1 ].get_text())[:-4])))
	print(weight)

	#Height
	height_stat = soup.select('table.roundy tr td.roundy b a[href*="height"]')[ 0 ].parent.parent
	pkmn_data.append(float(((height_stat.select( 'table tr td' )[ 1 ].get_text())[:-4])))

	#EvolveLine
	current_form = soup.select('tbody tr td a[class="mw-selflink selflink"]').parent.parent.parent.parent
	prev_level = current_form.previous_sibling.select('a[href*="Level"')

	next_forms = []



	return pkmn_data

def allPokemonStats():
	pass

def writeToDB():
	pass


getPokemonData("/wiki/Venusaur_(Pokémon)")