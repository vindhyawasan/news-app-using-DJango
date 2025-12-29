from django.shortcuts import render
import requests
import json

def weather(request):
    if request.method == 'POST':
        search = request.POST.get('search')  # ✅ fixed case

        url = f"https://newsapi.org/v2/everything?q={search}&from=2025-11-28&sortBy=publishedAt&apiKey=bc3c5afc97c24531bb4d8da1ecd562f5"
        r = requests.get(url)
        news = json.loads(r.text)

        if news.get("articles"):
            articles = news["articles"][0]
            print(news)
            return render(request, 'index.html', {"article": articles})

    return render(request, 'index.html')
