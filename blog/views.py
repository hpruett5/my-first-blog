from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request) -> HttpResponse:
    template = loader.get_template('post_list.html')
    posts = Post.objects.filter(published_date_lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})