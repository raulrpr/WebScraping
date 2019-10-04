import requests

url = "http://dilbert.com"

print("\tRequesting: ", url)
res = requests.get(url)
res.raise_for_status()
print("\t\tHTML result = ", res.status_code)

fileName = "Dilbert.html"
print("\tSaving image to %s..." % fileName)
imageFile = open(fileName, 'wb')
for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()

