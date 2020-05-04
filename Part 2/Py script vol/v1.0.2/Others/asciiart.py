# https://www.makeschool.com/academy/track/standalone/make-games-with-python-soy/ascii-art

import requests

text = input('ASCII Art Text > ')

r = requests.get(f'http://artii.herokuapp.com/make?text={text}')
print(r.text)