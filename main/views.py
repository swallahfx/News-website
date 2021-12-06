from django.shortcuts import render
import requests
import json
news_api_request = requests.get("https://newsapi.org/v2/top-headlines?country=ng&apiKey=59fdad00595c4261babe74ab3822662c")
api = news_api_request.json()



def home(request):
    
    apin=api
   
    print(api, " ")

    return render(request, 'main/home.html' , {"api":apin})

def news(request):
    
    apin=api
   
    print(api, " ")

    return render(request, 'main/news.html' , {"api":apin})
