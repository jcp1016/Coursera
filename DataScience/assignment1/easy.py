import requests

response = requests.get('https://api.github.com/users/mbostock/repos')

assert response.status_code == 200

for repo in response.json():
    print '[{}] {}'.format(repo['language'], repo['name'])

