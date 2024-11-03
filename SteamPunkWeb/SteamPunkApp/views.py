from django.shortcuts import render, HttpResponse

# Create your views here.
def mainView(request):
    return render(request, "home.html")