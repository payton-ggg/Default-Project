import phonenumbers
from phonenumbers import geocoder, carrier

y = input("Input your number: ")

x = phonenumbers.parse(y, None)

region = geocoder.description_for_number(x, "en")

print(x, region)