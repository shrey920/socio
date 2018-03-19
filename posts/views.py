from django.views import generic
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import *
# Create your views here.

User= get_user_model()

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login'
    model=Post
    fields = ['title','text','image']

    def dispatch(self, request, *args, **kwargs):
        sender = request.user
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        if form.is_valid():
            form.save()
            return redirect('socio:home')

class EditPostView(LoginRequiredMixin,UpdateView):
    login_url = '/login'
    model=Post
    fields = ['title','text','image']

    def dispatch(self, request, *args, **kwargs):
        pk=kwargs['pk']
        if request.user != Post.objects.get(pk=pk).owner:
            return redirect('posts:allPosts')
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('socio:home')

class DeletePostView(LoginRequiredMixin, DeleteView):
    login_url = '/login'
    model = Post
    success_url = reverse_lazy('posts:allPosts')

    def dispatch(self, request, *args, **kwargs):
        pk=kwargs['pk']
        if request.user != Post.objects.get(pk=pk).owner:
            return redirect('posts:allPosts')
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)


class PostsView(LoginRequiredMixin, generic.ListView):
    login_url = '/login'
    template_name='posts/posts.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        p=set(self.request.user.post_owner.all())
        for friend in self.request.user.profile.friends.all():
            p=p.union(set(friend.post_owner.all()))
        return set(reversed(list(p)))

class LikePostView(LoginRequiredMixin, APIView):
    login_url =  '/login'
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, format=None):
        post=Post.objects.get(pk=pk)
        liked = False
        likes = int(post.likes.count())

        if request.user in post.likes.all():
            likes = likes-1
            liked = False
            post.likes.remove(request.user)
        else:
            liked = True
            likes = likes + 1
            post.likes.add(request.user)

        data = {
            'liked': liked,
            'likes': likes
        }
        return Response(data)
