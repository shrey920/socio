from django.views import generic
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class IndexView(generic.TemplateView):
    template_name='socio/index.html'

    def dispatch(self, request, *args, **kwargs):
        if str(request.user) is 'AnonymousUser':
            return render(request, self.template_name)
        else:
            return redirect('profiles:profileView',self.request.user)
