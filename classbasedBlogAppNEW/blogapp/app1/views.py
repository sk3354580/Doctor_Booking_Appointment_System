from django.shortcuts import render
from . models import Blogs
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class BlogsListview(ListView):
    model = Blogs
    template_name = 'blogs.html'
    context_object_name = 'blog'

class BlogsDetailview(DetailView):
    model = Blogs
    template_name = 'blogsdetail.html'
    context_object_name = 'blogsdetail'

class BlogsCreateview(CreateView):
    model = Blogs
    template_name = 'create_edit.html'
    fields = ['title','description']
    success_url = '/'

class BlogsUpdateview(UpdateView):
    model = Blogs
    template_name = 'create_edit.html'
    fields = ['title','description']
    success_url = '/'

class BlogsDeleteview(DeleteView):
    model = Blogs
    template_name = 'confirm.html'
    success_url = '/'