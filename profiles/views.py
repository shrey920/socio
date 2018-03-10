from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
# Create your views here.

User = get_user_model()

class ProfileView(generic.DetailView):
    template_name='profiles/profile_view.html'
    context_object_name = 'context'

    def get_object(self, queryset=Profile.objects):
        user=User.objects.get(username=self.kwargs['username'])
        valid=False
        try:
            profile=Profile.objects.get(user=user)
            if self.request.user == user:
                valid=True
        except:
            profile=None
        return {'profile' :profile,'user':user,'valid':valid}

class UpdateProfileView(generic.UpdateView):
    model=Profile
    fields=['firstName','lastName','bio','picture']

    def dispatch(self, request, *args, **kwargs):
        user=User.objects.get(pk=self.kwargs['pk'])
        if self.request.user != user:
            try:
                logout(request.user)
            except:
                pass
            return redirect('socio:home')
        else:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)

    def form_valid(self, form):
        user=User.objects.get(pk=self.kwargs['pk'])
        if form.is_valid():
            form.save()
            return redirect('profiles:profileView',user)
