from django.shortcuts import render
from .models import Post

# Create your views here.
def hello(request):
    all_posts = Post.objects.all()

    return render(request, 'blog/home.html', { 'all_posts': all_posts })

def post_detail(request, id):
    single_post = Post.objects.get(id=id)

    return render(request, 'blog/post-detail.html', { 'single_post': single_post })