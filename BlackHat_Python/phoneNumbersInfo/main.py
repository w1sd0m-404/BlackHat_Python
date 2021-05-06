import phonenumbers
from phonenumbers import geocoder

from test import number

ch_number=phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "tr"))

from phonenumbers import carrier

service_number=phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "tr"))

from phonenumbers import timezone

gb_number=phonenumbers.parse(number, "GB")
print(timezone.time_zones_for_number(gb_number))