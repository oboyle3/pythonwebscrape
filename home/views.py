from django.shortcuts import redirect, render
from bs4 import BeautifulSoup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import requests

from home.forms import AvailabilityForm
from home.models import Availability
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


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})






@login_required
def loggedin(request):
    user = request.user

    # Get or create the current availability
    try:
        current_availability = Availability.objects.get(user=user)
    except Availability.DoesNotExist:
        current_availability = None

    if request.method == "POST":
        form = AvailabilityForm(request.POST, instance=current_availability)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.user = user
            availability.save()
            return redirect("loggedin")  # refresh page after saving
    else:
        form = AvailabilityForm(instance=current_availability)

    return render(request, "home/loggedin.html", {
        "username": user.username,
        "form": form,
    })