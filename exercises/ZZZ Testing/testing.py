import random
import pycountry

country = random.choice(list(pycountry.countries)).name
print(country)