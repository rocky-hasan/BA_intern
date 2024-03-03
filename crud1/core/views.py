from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import RedirectView
from core.models import Student
from .forms import Addstudent


# Create your views here.

class home(View):

    def get(self, request):
        stu_data = Student.objects.all()
        return render(request, 'home.html', {'students': stu_data})


class add_student(View):
    def get(self, request):
        fm = Addstudent()
        return render(request, 'addstu.html', {'form': fm})

    def post(self, request):
        fm = Addstudent(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/")
        else:
            return render(request, 'addstu.html', {'form': fm})


class Delete_data(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        studata = Student.objects.get(id=id)
        studata.delete()
        return redirect('/')


class Edit_data(View):
    def get(self, request,id):
        pi=Student.objects.get(pk=id)
        fm=Addstudent(instance=pi)
        return render(request, 'edit.html', {'form': fm})

    def post(self,request,id):
        pi = Student.objects.get(id=id)
        fm = Addstudent(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/')


