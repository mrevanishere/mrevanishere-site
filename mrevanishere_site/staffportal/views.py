from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate, login



def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        render(request, '')
    else:
        render(request, 'blog/index.html')


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "staffportal/dashboard.html"