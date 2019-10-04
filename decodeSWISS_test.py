import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        json_str = """{
			"page": {

  "attributes": {
    "htmlTitle": "Select outbound flight | SWISS"
  },
  "category": {
  "category1": "book",
  "category2": "outbound",
  "category3": "",
  "category4": "",
  "category5": ""
}
,

  "pageInfo": {
    "pageId": "/book/outbound",
    "city": "barcelona",
    "country": "spain",
    "language": "en",
    "pageName": "outbound_page"
  }
},

  "user": {
    "profile": {
      "profileInfo": {
        "profileId": "",
        "profileType": ""
      }
    },
    "segment": [
      {
        "segmentId": "",
        "segmentType": "",
        "upgradeScore": ""
      }
    ]
  }
,

  "conversion": {
    "funnel": {
      "funnelName": "bbf",
      "funnelStep": "outbound"
    }
  },
  "filter": {
    "category": {
      "category1": "flight",
      "category2": "",
      "category3": "",
      "category4": "",
      "category5": ""
    },
    "element": [
      {
        "elementName": "origin",
        "elementType": "textfield",
        "elementValue": "userinput",
        "sectionName": "flight-one-way",
        "userInput": "BCN"
      },
      {
        "elementName": "destination",
        "elementType": "textfield",
        "elementValue": "userinput",
        "sectionName": "flight-one-way",
        "userInput": "ZRH"
      },
      {
        "elementName": "outbound-date",
        "elementType": "singleselector",
        "elementValue": "userinput",
        "sectionName": "flight-one-way",
        "userInput": "2017-12-01"
      },
      {
        "elementName": "adults",
        "elementType": "singleselector",
        "elementValue": "userinput",
        "sectionName": "flight-one-way",
        "userInput": "1"
      },
      {
        "elementName": "children",
        "elementType": "singleselector",
        "elementValue": "userinput",
        "sectionName": "flight-one-way",
        "userInput": "0"
      },
      {
        "elementName": "infants",
        "elementType": "singleselector",
        "elementValue": "userinput",
        "sectionName": "flight-one-way",
        "userInput": "0"
      },
      {
        "elementName": "class",
        "elementType": "singleselector",
        "elementValue": "userinput",
        "sectionName": "flight-one-way",
        "userInput": "y"
      },
      {
        "elementName": "airline",
        "elementType": "singleselector",
        "elementValue": "userinput",
        "sectionName": "flight-one-way",
        "userInput": "lx"
      }
    ],
    "filterInfo": {
      "complexity": "multiple",
      "criteria": "8",
      "logic": "literal",
      "term": "BCN-ZRH/from-2017-12-01/adults-1/children-0/infants-0/class-economy/al-LX",
      "type": "flight"
    },
    "result": {
      "elementName": "flightsdata",
      "iteration": "1",
      "numberDisplayed": "3",
      "numberReturned": "3",
      "sectionName": "Fri 01/12/2017 from EUR81"
    }
  },
  "product": [
    {
      "price": {
        "basePrice": "153,00",
        "currency": "eur"
      },
      "layover": [],
      "attributes": {
        "brand": "swiss",
        "variant": "",
        "quantity": "1"
      },
      "category": {
        "category1": "flight",
        "category2": "flight-one-way",
        "category3": "",
        "category4": "",
        "category5": ""
      },
      "productInfo": {
        "arrival": "2017-12-01 11:40:00",
        "bookingClass": "v",
        "bundle": [
          "eul",
          "euc",
          "euf"
        ],
        "departure": "2017-12-01 09:45:00",
        "destination": "zrh",
        "duration": "01:55:00",
        "origin": "bcn",
        "productId": "bcn-zrh 2017-12-01 09:45:00 flight-one-way",
        "productName": "bcn-zrh flight-one-way",
        "segment": [
          {
            "aircraft": "",
            "arrival": "2017-12-01 11:40:00",
            "departure": "2017-12-01 09:45:00",
            "destination": "zrh",
            "duration": "01:55:00",
            "flightAssociation": "1",
            "flightNumber": "1953",
            "isCodeshare": "0",
            "mCarrier": "lx",
            "number": "1",
            "oCarrier": "lx",
            "origin": "bcn",
            "segmentId": "bcn-zrh 2017-12-01 09:45:00"
          }
        ]
      }
    },
    {
      "price": {
        "basePrice": "380,00",
        "currency": "eur"
      },
      "layover": [],
      "attributes": {
        "brand": "swiss",
        "variant": "",
        "quantity": "1"
      },
      "category": {
        "category1": "flight",
        "category2": "flight-one-way",
        "category3": "",
        "category4": "",
        "category5": ""
      },
      "productInfo": {
        "arrival": "2017-12-01 11:40:00",
        "bookingClass": "d",
        "bundle": [
          "eux",
          "eub"
        ],
        "departure": "2017-12-01 09:45:00",
        "destination": "zrh",
        "duration": "01:55:00",
        "origin": "bcn",
        "productId": "bcn-zrh 2017-12-01 09:45:00 flight-one-way",
        "productName": "bcn-zrh flight-one-way",
        "segment": [
          {
            "aircraft": "",
            "arrival": "2017-12-01 11:40:00",
            "departure": "2017-12-01 09:45:00",
            "destination": "zrh",
            "duration": "01:55:00",
            "flightAssociation": "1",
            "flightNumber": "1953",
            "isCodeshare": "0",
            "mCarrier": "lx",
            "number": "1",
            "oCarrier": "lx",
            "origin": "bcn",
            "segmentId": "bcn-zrh 2017-12-01 09:45:00"
          }
        ]
      }
    },
    {
      "price": {
        "basePrice": "81,00",
        "currency": "eur"
      },
      "layover": [],
      "attributes": {
        "brand": "swiss",
        "variant": "",
        "quantity": "1"
      },
      "category": {
        "category1": "flight",
        "category2": "flight-one-way",
        "category3": "",
        "category4": "",
        "category5": ""
      },
      "productInfo": {
        "arrival": "2017-12-01 04:35:00",
        "bookingClass": "t",
        "bundle": [
          "eul",
          "euc",
          "euf"
        ],
        "departure": "2017-12-01 02:45:00",
        "destination": "zrh",
        "duration": "01:50:00",
        "origin": "bcn",
        "productId": "bcn-zrh 2017-12-01 02:45:00 flight-one-way",
        "productName": "bcn-zrh flight-one-way",
        "segment": [
          {
            "aircraft": "",
            "arrival": "2017-12-01 04:35:00",
            "departure": "2017-12-01 02:45:00",
            "destination": "zrh",
            "duration": "01:50:00",
            "flightAssociation": "1",
            "flightNumber": "1955",
            "isCodeshare": "0",
            "mCarrier": "lx",
            "number": "1",
            "oCarrier": "lx",
            "origin": "bcn",
            "segmentId": "bcn-zrh 2017-12-01 02:45:00"
          }
        ]
      }
    },
    {
      "price": {
        "basePrice": "270,00",
        "currency": "eur"
      },
      "layover": [],
      "attributes": {
        "brand": "swiss",
        "variant": "",
        "quantity": "1"
      },
      "category": {
        "category1": "flight",
        "category2": "flight-one-way",
        "category3": "",
        "category4": "",
        "category5": ""
      },
      "productInfo": {
        "arrival": "2017-12-01 04:35:00",
        "bookingClass": "z",
        "bundle": [
          "eux",
          "eub"
        ],
        "departure": "2017-12-01 02:45:00",
        "destination": "zrh",
        "duration": "01:50:00",
        "origin": "bcn",
        "productId": "bcn-zrh 2017-12-01 02:45:00 flight-one-way",
        "productName": "bcn-zrh flight-one-way",
        "segment": [
          {
            "aircraft": "",
            "arrival": "2017-12-01 04:35:00",
            "departure": "2017-12-01 02:45:00",
            "destination": "zrh",
            "duration": "01:50:00",
            "flightAssociation": "1",
            "flightNumber": "1955",
            "isCodeshare": "0",
            "mCarrier": "lx",
            "number": "1",
            "oCarrier": "lx",
            "origin": "bcn",
            "segmentId": "bcn-zrh 2017-12-01 02:45:00"
          }
        ]
      }
    },
    {
      "price": {
        "basePrice": "81,00",
        "currency": "eur"
      },
      "layover": [],
      "attributes": {
        "brand": "swiss",
        "variant": "",
        "quantity": "1"
      },
      "category": {
        "category1": "flight",
        "category2": "flight-one-way",
        "category3": "",
        "category4": "",
        "category5": ""
      },
      "productInfo": {
        "arrival": "2017-12-01 09:45:00",
        "bookingClass": "t",
        "bundle": [
          "eul",
          "euc",
          "euf"
        ],
        "departure": "2017-12-01 07:55:00",
        "destination": "zrh",
        "duration": "01:50:00",
        "origin": "bcn",
        "productId": "bcn-zrh 2017-12-01 07:55:00 flight-one-way",
        "productName": "bcn-zrh flight-one-way",
        "segment": [
          {
            "aircraft": "",
            "arrival": "2017-12-01 09:45:00",
            "departure": "2017-12-01 07:55:00",
            "destination": "zrh",
            "duration": "01:50:00",
            "flightAssociation": "1",
            "flightNumber": "1957",
            "isCodeshare": "0",
            "mCarrier": "lx",
            "number": "1",
            "oCarrier": "lx",
            "origin": "bcn",
            "segmentId": "bcn-zrh 2017-12-01 07:55:00"
          }
        ]
      }
    },
    {
      "price": {
        "basePrice": "270,00",
        "currency": "eur"
      },
      "layover": [],
      "attributes": {
        "brand": "swiss",
        "variant": "",
        "quantity": "1"
      },
      "category": {
        "category1": "flight",
        "category2": "flight-one-way",
        "category3": "",
        "category4": "",
        "category5": ""
      },
      "productInfo": {
        "arrival": "2017-12-01 09:45:00",
        "bookingClass": "z",
        "bundle": [
          "eux",
          "eub"
        ],
        "departure": "2017-12-01 07:55:00",
        "destination": "zrh",
        "duration": "01:50:00",
        "origin": "bcn",
        "productId": "bcn-zrh 2017-12-01 07:55:00 flight-one-way",
        "productName": "bcn-zrh flight-one-way",
        "segment": [
          {
            "aircraft": "",
            "arrival": "2017-12-01 09:45:00",
            "departure": "2017-12-01 07:55:00",
            "destination": "zrh",
            "duration": "01:50:00",
            "flightAssociation": "1",
            "flightNumber": "1957",
            "isCodeshare": "0",
            "mCarrier": "lx",
            "number": "1",
            "oCarrier": "lx",
            "origin": "bcn",
            "segmentId": "bcn-zrh 2017-12-01 07:55:00"
          }
        ]
      }
    }
  ]

		}"""

        import json
        dict = json.loads(json_str)
        print("Length of product is ", len(dict['product']))

        self.assertEqual(len(dict['product']), 6)


if __name__ == '__main__':
    unittest.main()
