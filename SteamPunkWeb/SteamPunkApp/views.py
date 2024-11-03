from django.shortcuts import render, HttpResponse

# Create your views here.
def mainView(request):
    return render(request, "home.html")

def about_page(request):
    return render(request, 'SteamPunkWeb/SteamPunkApp/templates/about_page.html')

def base(request):
    return render(request, 'SteamPunkWeb/SteamPunkApp/templates/base.html')

def chat_page(request):
    return render(request, 'SteamPunkWeb/SteamPunkApp/templates/chat_page.html')

def home(request):
    return render(request, 'SteamPunkWeb/SteamPunkApp/templates/home.html')

def transition_page(request):
    return render(request, 'SteamPunkWeb/SteamPunkApp/templates/transition_page.html')

def Tutorial_page(request):
    return render(request, 'SteamPunkWeb/SteamPunkApp/templates/Tutorial_page.html')

def welcome_page(request):
    return render(request, 'SteamPunkWeb/SteamPunkApp/templates/welcome_page.html')