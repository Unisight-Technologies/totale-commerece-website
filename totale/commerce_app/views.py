from django.shortcuts import render, redirect
from django.views.generic import View
from . import models
from django.contrib import messages
# Create your views here.

class Homepage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'index.html')


    def post(self, request, *args, **kwargs):
        print('hii')

        print('hello')
        data = request.post
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        course = data.get('course')
        message = data.get('message')

        admission = models.AdmissionModel.objects.create(
                        name=name,
                        email=email,
                        phone=phone,
                        course=course,
                        message=message,)

        admission.save()
        return redirect('index')





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
