import csv
import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd


url = 'https://www.mitsubishi-motors.ca/en/vehicle/showroom/outlander/2019/'
page = requests.get(url)
print(page.status_code)

soup = BeautifulSoup(page.text, 'html.parser')



# from datetime import datetime
dt_object = datetime.datetime.now()

# all Vehicles
specifications = soup.find('section', class_="specifications l-row background-white")
ul = specifications.find_all('div', class_='vcontainer')
clas = ul

# Create a file Price, give headers: Price and Name of the shoe
f = csv.writer(open('car.csv', 'a', encoding='utf-8'))
f.writerow(['Car Model', 'Price', 'Date'])

# To get all specification for each Outlander model
name = []
price = []

for i in clas:
    name.append(i.h2.text)
    price.append(i.h3.text)
    f.writerow([i.h2.text, i.h3.text, dt_object])


df = pd.DataFrame({'name': name, 'price': price})

print(df)
