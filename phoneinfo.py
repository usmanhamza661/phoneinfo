import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import time
import os
import pyfiglet

# colors
green = "\033[1;32m"
blue = "\033[1;34m"
red = "\033[1;31m"
reset = "\033[0m"

os.system("clear")

banner = pyfiglet.figlet_format("PHONE INFO")
print(blue + banner + reset)

print("Coder : USMAN")
print("-" * 40)

print("You can enter number with or without country code")
print("Example: 08012345678 or +2348012345678\n")

number = input(green + "Enter phone number: " + reset)

try:
    # AUTO COUNTRY DETECT (Nigeria)
    if number.startswith("0"):
        number = "+234" + number[1:]

    phone = phonenumbers.parse(number)

    print("\nChecking number...")
    time.sleep(2)

    print("Country  :", geocoder.description_for_number(phone, "en"))
    print("TimeZone :", timezone.time_zones_for_number(phone))
    print("Network  :", carrier.name_for_number(phone, "en"))

except:
    print(red + "Invalid phone number!" + reset)