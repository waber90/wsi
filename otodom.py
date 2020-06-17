from bs4 import BeautifulSoup
import requests

def make_url(city):
    url="https://www.otodom.pl/sprzedaz/"
        
    url=url+city.replace(" ","%20")
    
    return url
    
def otodom_scrap(url, recordNumber=0, option=0):
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,'html.parser')
 
    offers = []
    for post in soup.find_all("div", {"class": "offer-item-details"}):
        offer = {
            "1.uri": post.find_next("a")["href"],
            "2.title": post.find_next("span", {"class": "offer-item-title"}).text,
            "3.price": post.find_next("li", {"class": "offer-item-price"}).text,
            "4.measurement":post.find_next("strong",{"class":"visible-xs-block"}).text,
            "5.localization":post.find_next("p",{"class":"text-nowrap"}).text,
            "6.pricePerMeter":post.find_next("li",{"class":"hidden-xs offer-item-price-per-m"}).text

        }

        offers.append(offer)

    if option==1:
        return offers[int(recordNumber)]

    return offers
