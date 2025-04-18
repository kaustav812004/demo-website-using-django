from django.shortcuts import render
from .models import Blog
# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs':blogs})

def blog(request, pk):
    blogs = Blog.objects.get(id=pk)
    return render(request, 'blogs.html', {'blogs': blogs})