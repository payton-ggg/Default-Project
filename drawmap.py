import folium 
import requests 
import random
from pyfiglet import Figlet

def random_ip():
	ip_1 = random.randint(0, 255)
	ip_2 = random.randint(0, 255)
	ip_3 = random.randint(0, 255)
	ip_4 = random.randint(0, 255)

	print(ip_1, ip_2, ip_3, ip_4, sep='.')

def get_info_by_ip(ip='127.0.0.1'):
	try:
		response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

		data = {
		'[IP]':response.get('query'),
		'[Int prov]': response.get('isp'),
		'[Org]': response.get('org'),
		'[Country]':response.get('country'),
		'[Region Name]':response.get('regionName'),
		'[City]':response.get('city'),
		'[ZIP]':response.get('zip'),
		'[Lat]':response.get('lat'),
		'[Lon]':response.get('lon')
		}

		for k, v in data.items():
			print(f'{k} : {v}')

	except requests.exceptions.ConnectionError:
		print('[!] Check your Connection')
		
	map = folium.Map(location=[response.get('lat'), response.get('lon')])
	map.save(f'{response.get("query")}_{response.get("city")}.html')
	
	print(map)

def main():
	preview_text = Figlet(font='slant')
	print(preview_text.renderText('IP INFO'))
	ip = input('Enter a target IP: ')

	if ip == 'get_random_ip':
		random_ip()

		ip = input('Enter a target IP: ')
	else:
		pass


	get_info_by_ip(ip=ip)

if __name__ == '__main__':
	main()