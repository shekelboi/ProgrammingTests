import requests as requests
from random import randint

BASE_URL = 'https://collectionapi.metmuseum.org/public/collection/v1/'
OBJECTS = 'objects'
DEPARTMENTS = 'departments'
SEARCH = 'search'

# Finding the department with the name 'Asian Art'
response = requests.get(BASE_URL + DEPARTMENTS)
asian_art = [dept for dept in response.json()['departments'] if dept['displayName'] == 'Asian Art'][0]['departmentId']
print(asian_art)

params = {
    'departmentIds': asian_art
}
# Retrieving all the objects within the department
response = requests.get(BASE_URL + OBJECTS, params=params)
print(response.json()['total'])

# Finding the department with the name 'Arms and Armor' or 'Musical Instruments'
response = requests.get(BASE_URL + DEPARTMENTS)
selected_categories = [dept['departmentId'] for dept in response.json()['departments'] if
                       dept['displayName'] in ['Arms and Armor', 'Musical Instruments']]
params = {
    'departmentIds': '|'.join(map(str, selected_categories))
}
# Retrieving all the objects within the department
response = requests.get(BASE_URL + OBJECTS, params=params)
print(response.json()['total'])

params = {
    'q': 'missile'
}
response = requests.get(BASE_URL + SEARCH, params=params)
missiles = response.json()['objectIDs']

# Selecting 5 random objects
selected_indexes = set()
while 16 > len(selected_indexes):
    r = randint(0, len(missiles) - 1)
    if r not in selected_indexes:
        selected_indexes.add(r)

for i in selected_indexes:
    response = requests.get(f'{BASE_URL}{OBJECTS}/{missiles[i]}')
    data = response.json()
    print(f'Title: {data["title"]}, department: {data["department"]}')

# Download all the preview images of artifacts related to Malagasy culture
params = {
    'q': 'Malagasy'
}
response = requests.get(BASE_URL + SEARCH, params=params)
object_ids = response.json()['objectIDs']
for id in object_ids:
    response = requests.get(f'{BASE_URL}{OBJECTS}/{id}')
    data = response.json()
    if 'primaryImageSmall' in data:
        image_url = data['primaryImageSmall']
        print(image_url)
        if image_url:
            content = requests.get(image_url).content
            with open(f'{id}.jpg', 'wb') as file:
                file.write(content)

params = {
    'q': 'Afghan',
    'isOnView': 'true',
    'geoLocation': 'Asia'
}
response = requests.get(BASE_URL + SEARCH, params=params)
object_ids = response.json()['objectIDs']
for id in object_ids:
    data = requests.get(f'{BASE_URL}{OBJECTS}/{id}').json()
    print(', '.join((data['title'], data['city'], data['country'])))
