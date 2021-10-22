##Roket Fırlatış Takvim -parser-
#Mehmet Kahya 22.10.2021
import requests
from bs4 import BeautifulSoup
 
page = requests.get('https://everydayastronaut.com/upcoming-launches/')
soup = BeautifulSoup(page.content, 'html.parser')
 

total = soup.find_all("div", class_="cs-entry__inner cs-entry__content cs-overlay-content")

for total in total:
  roket = total.find("h2", class_="cs-entry__title upcoming-launches-counter").text
  zaman = total.find("div", class_="t-minus-bottom cs-meta-category article-launch-date launch-time").text
  #print(roket,zaman,"\n")
  print("""
           {0}                
           {1}      
  ###########################
  """.format(roket,zaman))
