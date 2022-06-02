from time import localtime, time
from tokenize import Number
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
Number=input("Enter Your No. with +__: ")
phone=phonenumbers.parse(Number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)
