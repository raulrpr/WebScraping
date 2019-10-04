from bs4 import BeautifulSoup
import requests
from datetime import date, timedelta
import time

# Build list of backward last week dates, starting from today
base = date.today()
date_list = (base - timedelta(days=x) for x in range(0, 7))

# List of saved image file names
imagesFileNames = [];

# For every date in the list...
for dt in date_list:
    strip_date = dt.strftime("%Y-%m-%d") # YYYY-mm-dd

    # Format the url depending on the date
    url = "http://dilbert.com/strip/{0}".format(strip_date)

    print("\tRequesting: ", url)
    req = requests.get(url)
    req.raise_for_status()
    print("\t\tHTML result = ", req.status_code)

    soup = BeautifulSoup(req.text, 'html.parser')
    comicElem = soup.select('.img-comic-link > img')

    # Get the image url to download + the strip title
    comicUrl = comicElem[0].get('src')
    comicTitle = comicElem[0].get('alt')

    # Download the image...
    print('\tDownloading image %s...' % comicUrl)
    res = requests.get(comicUrl)
    res.raise_for_status()

    # Save the image to disk...
    import os
    os.makedirs('dilbert', exist_ok=True)   # store comics in ./dilbert

    # Build the file name path...
    imageFileName = os.path.join('dilbert', strip_date + " - " + comicTitle + ".png")
    imagesFileNames.append(imageFileName)

    print("\tSaving image to %s..." % imageFileName)
    imageFile = open(imageFileName, 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

# Finally, open the folder where the strips were stored
os.startfile('dilbert')

# and open the first comic strip after a few seconds
time.sleep(5)
os.startfile(imagesFileNames[0])
