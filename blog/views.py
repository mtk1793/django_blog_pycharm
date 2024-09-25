from django.shortcuts import render
from datetime import date
all_posts = [
    {
        'slug':'learning-django',
        'title':'Learning',
        'author':'Mtk',
        'date':date.today(),
        'image':'django.png',
        'short_description':'This is the',
        'content':'This is lorem ipsum dolor sit'
    },
    {
          'slug':'learning-django',
        'title':'Learning',
        'author':'Mtk',
        'date':date.today(),
        'image':'master.png',
        'short_description':'This is the',
        'content':'This is lorem ipsum dolor sit'
    },
    {
          'slug':'learning-django',
        'title':'Learning',
        'author':'Mtk',
        'date':date.today(),
        'image':'ml.png',
        'short_description':'This is the',
        'content':'This is lorem ipsum dolor sit'
    },
    {
        'slug': 'learning-django',
        'title': 'Learning',
        'author': 'Mtk',
        'date': date.today(),
        'image': 'python.png',
        'short_description': 'This is the',
        'content': 'This is lorem ipsum dolor sit'
    }
]
# Create your views here.

def get_date(post):
    return post['date']
def index(request):
    sorted_posts = sorted(all_posts,key = get_date)
    latest_posts = sorted_posts[-2:]
    return render(request, 'blog/index.html', {
        'latest_posts': latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html')


def single_post(request,slug):
    return render(request, 'blog/post-detail.html')
