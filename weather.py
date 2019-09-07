from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.met.ie/forecasts/dublin'

#open connection and download html
uClient = uReq(my_url)
page_html = uClient.read()

page_soup = soup(page_html, "html.parser")

for_info = page_soup.find(class_="forecast")

#get relevent data and put in variables
for_time = for_info.p
for_today = for_info.p.find_next_sibling('p')
for_tonight = for_today.find_next_sibling('p')
for_pollen = for_tonight.find_next_sibling('p')
for_uv = for_pollen.find_next_sibling('p').find_next_sibling('p')
for_tomorrow = for_uv.find_next_sibling('p').find_next_sibling('p')

#print forecast
print(for_time.text)
print("TODAY")
print(for_today.text)
print("TONIGHT")
print(for_tonight.text)
print("Pollen forecast " + for_pollen.text.strip())
print("Solar UV index: " + for_uv.text)
print("TOMORROW")
print(for_tomorrow.text)