from django.shortcuts import render, redirect
from django.views.generic import View
from . import models
from django.contrib import messages
from . import mailHandler
# Create your views here.

class Homepage(View):
    def get(self, request, *args, **kwargs):
        context = {
            'unsubmitted':True
        }

        return render(request, 'index.html', context)


    def post(self, request, *args, **kwargs):
        data = request.POST
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
                        message=message,
                        )

        admission.save()
        messages.success(request, "Your request has been successfully submitted. We will get back to you soon.")
        mailHandler.sendMailToUser(name, email)
        mailHandler.sendMailAdmission(name, email, phone, message, course)

        context={
            'unsubmitted':False
        }
        return render(request, 'index.html', context)

class Aboutpage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'about.html')


class Contactpage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'contact.html')

    def post(self, request, *args, **kwargs):


        data = request.POST
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        query = models.Query.objects.create(
            name=name,
            email=email,
            message=message

        )
        query.save()
        messages.success(request, "Your request has been successfully submitted. We will get back to you soon.")
        mailHandler.sendMailToUser(name, email)
        mailHandler.sendMailQuery(name, email, message)
        context={
            'unsubmitted':False
        }
        return render(request, 'index.html', context)


class Blogpage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'blog.html')

class Coursespage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'courses.html')

class Teacherpage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'teacher.html')
