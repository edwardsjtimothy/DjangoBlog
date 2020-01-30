from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
      "author": "Tim",
      "title": "First Post",
      "content": "The dog ran up the hill.",
      "data_posted": "January 30th 2020"
    },
    {
      "author": "Zorp",
      "title": "Second Post",
      "content": "The Fox ran up the hill.",
      "data_posted": "January 30th 2020"
    }
]

def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")