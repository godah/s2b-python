from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

# Create your views here.
def index(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'index.html', {'posts': posts})

