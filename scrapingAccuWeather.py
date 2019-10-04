from bs4 import BeautifulSoup
import requests


dict_url = {
        "Baar"          : "https://www.accuweather.com/en/ch/baar/316344/current-weather/316344",
        "Bern"          : "https://www.accuweather.com/en/ch/bern/312122/current-weather/312122",
        "Geneva"        : "https://www.accuweather.com/en/ch/geneva/313082/current-weather/313082",
        "Lausanne"      : "https://www.accuweather.com/en/ch/lausanne/316303/current-weather/316303",
        "Zurich"        : "https://www.accuweather.com/en/ch/zurich/316622/current-weather/316622",
        "Frankfurt"     : "https://www.accuweather.com/en/de/frankfurt/60311/current-weather/168720",
        "München"       : "https://www.accuweather.com/en/de/munich/80331/current-weather/178086",
        "Barcelona"     : "https://www.accuweather.com/en/es/barcelona/307297/current-weather/307297",
        "Madrid"        : "https://www.accuweather.com/en/es/madrid/308526/current-weather/308526",
        "Bratislava"    : "https://www.accuweather.com/en/sk/bratislava/297345/current-weather/297345",
        "Manila"        : "https://www.accuweather.com/en/ph/manila/264885/current-weather/264885",
        "Singapore"     : "https://www.accuweather.com/en/sg/singapore/300597/current-weather/300597",
        "Cluj-Napoca"   : "https://www.accuweather.com/en/ro/cluj-napoca/287713/current-weather/287713"
    }

results = [];

for city, url in dict_url.items():
    print("   Requesting: ", url)
    req = requests.get(url)
    req.raise_for_status()
    print("   HTML result = ", req.status_code)

    # print(req.text)
    #print("Saving raw HTML into file...")
    #with open("AccuWeather.html", "w", encoding='utf-8') as f:
    #    print(req.text, file=f)

    print("   Parsing response with BeautifulSoup...")
    soup = BeautifulSoup(req.text, 'html.parser')

    div_forecasts = soup.select('div [class="forecast"]')
    temp = div_forecasts[0].findChild(name="span", attrs={'class':'large-temp'},  recursive=True)
    weather = div_forecasts[0].findChild(name="span", attrs={'class':'cond'},  recursive=True)

    results.append("Current temperature in {0} is {1}: \t{2}".format(city.ljust(11), temp.text, weather.text))

# Finally, print all temperatures
for item in results:
    print(item)