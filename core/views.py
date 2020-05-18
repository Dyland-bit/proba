from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import *

# Create your views here.

class HomeView(ListView):
    model = Buys
    paginate_by = 10
    template_name = "home.html"
