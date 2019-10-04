from bs4 import BeautifulSoup
import requests
from datetime import date

inpDt = date(2017, 12, 4)
origin = "BCN"
destination = "ZRH"

# https://www.swiss.com/es/en/Book/Outbound/BCN-ZRH/from-2017-12-04
urlFrom = "https://www.swiss.com/es/en/Book/Outbound/{1}-{2}/from-{0}".format(inpDt.strftime("%Y-%m-%d"), origin, destination)

print("Requesting: ", urlFrom)

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

req = requests.get(urlFrom, headers=headers)
req.raise_for_status()
print("HTML result = ", req.status_code)

# print(req.text)
print("Saving raw HTML into file...")
with open("Swiss.html", "w", encoding='utf-8') as f:
    print(req.text, file=f)

print("Prsing response with BeautifulSoup...")
soup = BeautifulSoup(req.text, 'html.parser')

print("1st approach : look for <h3> tags...")
h3_tags = soup.find_all('h3');

# <h3>Monday 30/10/2017, Barcelona (BCN) ab 06:30, Zurich (ZRH) an 08:15.  Economy from EUR 98.  Business from EUR 270. Operated by SWISS. </h3>
sentinel = inpDt.strftime("%d/%m/%Y")  # dd/mm/YYYY

for h3 in h3_tags:
    candidate_h3 = repr(h3)
    if candidate_h3.find(sentinel) >= 0:
        print(candidate_h3);

# also the json in html?
print("\r\n")
print("2nd approach: Regex + JSON...")
import re

pattern = re.compile('window.lhgData')
script_tag = soup.find('script', text = pattern)
scr = script_tag.text

#print(scr)
json_content = scr.split('window.lhgData = ')[1].replace(';', '')
#print(json_content)

import json
dict = json.loads(json_content)
products = dict['product']
for prod in products:
    print('Flight {0}{1} from {2} departure at {3} to {4} arrival at {5} (duration: {6}) for {7} {8} ({9})'.format(
        prod['productInfo']['segment'][0]['mCarrier'].upper(),
        prod['productInfo']['segment'][0]['flightNumber'],
        prod['productInfo']['origin'].upper(),
        prod['productInfo']['departure'],
        prod['productInfo']['destination'].upper(),
        prod['productInfo']['arrival'],
        prod['productInfo']['duration'],
        prod['price']['basePrice'],
        prod['price']['currency'].upper(),
        prod['productInfo']['bookingClass']
        ))
#print(dict)
