from bs4 import BeautifulSoup
import requests

search_target = "sr71+blackbird"

url = "https://www.google.es/search?tbm=isch&q=" + search_target

print("\tRequesting: ", url)
req = requests.get(url)
req.raise_for_status()
print("\tHTML result = ", req.status_code)

print("\tParsing response with BeautifulSoup...")
soup = BeautifulSoup(req.text, 'html.parser')

images = [img for img in soup.findAll('img')]
print(str(len(images)) + " images found.")

import os
os.makedirs(search_target, exist_ok=True)  # store images in ./search

print('Downloading images to search directory.')
image_links = [each.get('src') for each in images]
for i in range(0, len(image_links)):
    print("Downloading %s..." % image_links[i])
    res = requests.get(image_links[i])
    req.raise_for_status()

    file_path = os.path.join(search_target, str(i).rjust(4, '0') + ".png")
    print("\tSaving %s..." % file_path)
    with open(file_path, "wb") as f:
        f.write(res.content)

