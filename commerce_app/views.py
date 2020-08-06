from django.shortcuts import render, redirect
from django.views.generic import View
from . import models
from django.contrib import messages
# Create your views here.

class Homepage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'index.html')
