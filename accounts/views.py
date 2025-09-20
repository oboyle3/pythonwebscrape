from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # creates user with hashed password
            return redirect('login')  # built-in login view
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})
