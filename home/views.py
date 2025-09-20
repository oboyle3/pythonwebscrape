from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def stjoes(request):
    return render(request, 'home/stjoes.html')

def scrape_countries(request):
    url = "https://www.scrapethissite.com/pages/simple/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    #Extract Countries
    countries = []
    for country in soup.find_all("div",class_="country"):
        name = country.find("h3",class_="country-name").get_text(strip=True)
        

        countries.append({
            "name": name,
            
        })
    return render(request,"home/countries.html", {"countries":countries})

