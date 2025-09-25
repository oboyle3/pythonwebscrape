from django.shortcuts import redirect, render
from bs4 import BeautifulSoup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import BankAccount, UserProfile
from django.contrib.auth.decorators import login_required
import requests

from home.forms import AvailabilityForm, FavoriteGolferForm, TeamForm
from home.models import Availability, Profile
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

    # Availability logic
    try:
        current_availability = Availability.objects.get(user=user)
    except Availability.DoesNotExist:
        current_availability = None

    if request.method == "POST" and "availability_submit" in request.POST:
        form = AvailabilityForm(request.POST, instance=current_availability)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.user = user
            availability.save()
            return redirect("loggedin")
    else:
        form = AvailabilityForm(instance=current_availability)

    # Favorite team logic
    profile, created = Profile.objects.get_or_create(user=user)
    if request.method == "POST" and "team_submit" in request.POST:
        team_form = TeamForm(request.POST, instance=profile)
        if team_form.is_valid():
            team_form.save()
            print("hello")
            return redirect("loggedin")
    else:
        team_form = TeamForm(instance=profile)

    return render(request, "home/loggedin.html", {
        "username": user.username,
        "form": form,
        "team_form": team_form,
        "profile": profile,
    })





@login_required
def loggedin(request):
    account = BankAccount.objects.get(user=request.user)
    return render(request, 'home/loggedin.html', {
        'username': request.user.username,
        'balance': account.balance,
    })




def select_favorites(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = FavoriteGolferForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('html/loggedin')  # or wherever you want
    else:
        form = FavoriteGolferForm(instance=profile)

    return render(request, 'home/select_favorites.html', {'form': form})