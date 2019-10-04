from bs4 import BeautifulSoup
import requests

url = "https://www.barcelona-airport.com/eng/flight-arrival/VY9460"

print("   Requesting: ", url)
req = requests.get(url)
req.raise_for_status()
print("   HTML result = ", req.status_code)

# print(req.text)
# print("Saving raw HTML into file...")
# with open("BCNArrival.html", "w", encoding='utf-8') as f:
#    print(req.text, file=f)

print("   Parsing response with BeautifulSoup...")
soup = BeautifulSoup(req.text, 'html.parser')

#div_status = soup.select('div [id="flight_status_G"]')[0]
div_status = soup.find('div', id=lambda x: x and x.startswith('flight_status'))
status = [x for x in div_status.children if x.name == 'h2'][0].text

div_arrival = soup.select('div [id="flight_arr"]')[0]
bs= div_arrival.findChildren('b')
current  = "{0} {1}".format(bs[0].text,
                            bs[0].next_sibling.next_sibling.text)
scheduled = bs[1].text

#Finally
print("Flight status is: ", status)
print(current)
print(scheduled)