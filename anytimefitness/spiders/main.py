import scrapy
from anytimefitness.items import Product
from lxml import html
import requests

class AnytimefitnessSpider(scrapy.Spider):
    name = "anytimefitness"
    start_urls = ["https://example.com"]

    def parse(self, response):
        parser = html.fromstring(response.text)

        headers = {
            'sec-ch-ua-platform': '"Linux"',
            'Referer': 'https://www.anytimefitness.com/find-gym/',
            'x-dtpc': '6$589709489_503h5vEMHPLIOBRCICOBVACVRMOSNAMUOAQASF-0e0',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
        }

        items = requests.get('https://www.anytimefitness.com/wp-json/anytime/v1/map-locations', headers=headers).json()
        for item in items:
            item_address = item.get('content', {})
            latitude = item.get('latitude', None)
            longitude = item.get('longitude', None)
            address = item_address.get('address', '')
            city = item_address.get('city', '')
            state = item_address.get('state', '')
            country = item_address.get('country', '')
            directions_url = item_address.get('directions_url', '')
            yield Product(
                **{
                    'latitude': latitude,
                    'longitude': longitude,
                    'address': address,
                    'city': city,
                    'state': state,
                    'country': country,
                    'directions_url': directions_url,
                }
                )
            
