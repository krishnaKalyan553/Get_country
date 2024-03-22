import geoip2.database
from django.conf import settings
import os
base_dir = settings.BASE_DIR
db_path = os.path.join(base_dir, 'geo_targetting', 'GeoLite2-City.mmdb')

import logging

logger = logging.getLogger(__name__)


class GeoLocationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.reader = geoip2.database.Reader(db_path)

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        # ip_address = '2405:201:c41f:e1ad:2208:4488:39b5:2970'
        try:
            location = self.reader.city(ip_address)
            country = location.country.name
            city = location.city.name
            request.country = country
            request.city = city
        except Exception as e:
            request.country = e
            print(f"Error: {e}")

        response = self.get_response(request)
        return response