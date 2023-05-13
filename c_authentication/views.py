from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class UserLoginView(TemplateView):
    template_name = "authentication/login.html"


class UserRegisterView(TemplateView):
    template_name = "authentication/signup.html"
