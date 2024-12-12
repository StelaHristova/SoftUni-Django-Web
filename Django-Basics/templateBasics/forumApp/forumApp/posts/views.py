from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    context = {
        "current_time": datetime.now(),
        "person": {
            "age": 20,
            "height": 190,
        },
        "ids": ["43c3342c34", "4c3c34c", "343c4c3c"],
        "some_text": "Hello my Name is Stela and i am tired",
        "users": [
            "Pesho",
            "Ivan",
            "Stamat",
            "Maria",
            "Magdalena"
        ]
    }
    return render(request, 'base.html', context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to create django project?",
                "author": "Stela Hristova",
                "content": "I **really** don`t <i>know</i> how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project?",
                "author": "",
                "content": "###I really don`t know how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project?",
                "author": "Stela Hristova",
                "content": "",
                "created_at": datetime.now(),
            },
        ]
    }

    return render(request, 'posts/dashboard.html', context)

