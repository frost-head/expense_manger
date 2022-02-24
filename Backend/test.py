#to test the api

from requests import post, get

post('http://192.168.43.192:5000/createuser', data={'Name':'Astha', 'Username':'MySunshine','Password':'tes2'} )

data = get('http://192.168.43.192:5000/createuser' ).json()

print(data)