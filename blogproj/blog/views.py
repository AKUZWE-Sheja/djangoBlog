from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author': 'Alice Johnson',
        'title': 'The Beauty of Nature',
        'content': 'Nature is full of wonders, from the tallest mountains to the deepest oceans. Exploring the outdoors can rejuvenate the spirit.',
        'date_posted': '2024-09-20'
    },
    {
        'author': 'Bob Smith',
        'title': 'Tech Innovations in 2024',
        'content': 'This year has seen remarkable advancements in technology, including AI and renewable energy solutions that are changing our world.',
        'date_posted': '2024-09-22'
    },
    {
        'author': 'Catherine Lee',
        'title': 'Healthy Living Tips',
        'content': 'Maintaining a balanced diet and regular exercise can significantly improve your quality of life. Here are some tips to get started.',
        'date_posted': '2024-09-25'
    },
]


def home(request):
    context = {
        'posts' : Post.objects.all()
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
