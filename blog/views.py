from django.shortcuts import render
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class blog_list_view(ListView):
    model = Post
    template_name = 'home.html'

class blog_detail_view(DetailView):
    model = Post
    template_name = 'post_detail.html'

class blog_create_view(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = [ 'title', 'author', 'body']

class blog_update_view(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class blog_delete_view(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class blog_create_comment(CreateView):
    model = Comment
    template_name = 'new_comment.html'
    fields = [ 'post', 'name', 'body']
    success_url = reverse_lazy('home')

