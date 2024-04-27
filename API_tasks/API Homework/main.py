import shutil
import requests
import os
import zipfile

SHIBE_FOLDER = 'dog_pics'

MIN = 5
MAX = 15
RANDOM_URL = f'https://www.randomnumberapi.com/api/v1.0/random'
params = {
    'min': MIN,
    'max': MAX + 1
}
response = requests.get(RANDOM_URL, params=params)
random_number = response.json()[0]
print(random_number)

SHIBE_URL = f'https://shibe.online/api/shibes'
params = {
    'count': random_number
}
response = requests.get(SHIBE_URL, params=params)
images = response.json()

if os.path.exists(SHIBE_FOLDER):
    shutil.rmtree(SHIBE_FOLDER)

os.mkdir(SHIBE_FOLDER)

for image_url in images:
    image_file_name = image_url.split('/')[-1]
    with open(os.path.join(SHIBE_FOLDER, image_file_name), 'wb') as file:
        file.write(requests.get(image_url).content)

ZIP_NAME = 'out.zip'
with zipfile.ZipFile(ZIP_NAME, 'w', zipfile.ZIP_DEFLATED) as file:
    images = os.listdir(SHIBE_FOLDER)
    for image_name in images:
        file.write(os.path.join(SHIBE_FOLDER, image_name), image_name)

with open(ZIP_NAME, 'rb') as file:
    files = {
        'file': file
    }

    data = {
        'expires': '48'
    }

    response = requests.post('https://0x0.st/', files=files, data=data)
    print(response.text)

os.remove(ZIP_NAME)
shutil.rmtree(SHIBE_FOLDER)
