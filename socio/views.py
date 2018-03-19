from django.views import generic
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class IndexView(generic.TemplateView):
    def dispatch(self, request, *args, **kwargs):
        try:
            if request.user.profile:
                return redirect('posts:allPosts')
        except:
            return redirect('profiles:profileView',request.user)
