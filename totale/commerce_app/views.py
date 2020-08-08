from django.shortcuts import render, redirect
from django.views.generic import View
from . import models
from django.contrib import messages
# Create your views here.

class Homepage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'index.html')


class Aboutpage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'about.html')


class Contactpage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'contact.html')


class Blogpage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'blog.html')

class Coursespage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'courses.html')

class Teacherpage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'teacher.html')
