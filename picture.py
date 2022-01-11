import requests

req = requests.get('https://www.nme.com/wp-content/uploads/2021/07/RickAstley2021.jpg')
fin = open('input.jpg', 'wb')
fin.write(req.content)
