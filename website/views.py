from django.shortcuts import render


def home_website(request):
    return render(request, 'website/home.html')
