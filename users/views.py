from typing import ItemsView
from django.contrib import messages
from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic import TemplateView, ListView
from django.urls import reverse
from users.forms import EmployeeForm, PanchayathForm, EndUserForm, NewsForm, SalaryForm
from users.models import Employee, EndUser, News, Salary
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class HomeView(TemplateView):
    template_name = 'home.html'


def index(request):
        current_user = request.user
        panchayath = None
        employee = None
        endusers = None
        # admin = None

        #check if current_user is panchayath

        try:
            panchayath = current_user.panchayath
        except:
            pass

        if panchayath:
        
            employees = Employee.objects.filter(panchayath_name= request.user.panchayath)
            endusers = EndUser.objects.filter(panchayath_name= request.user.panchayath)
            return render(request, 'index_panchayath.html', {'employees':employees,'endusers':endusers})

        #check if current_user is employee

        try:
            employee = current_user.employee
        except:
            pass

        if employee:
            print(request.user.employee.panchayath_name)
            endusers= EndUser.objects.filter(panchayath_name= request.user.employee.panchayath_name)
            return render(request,'index_employee.html', {'enduser': endusers})

         #check if current user is end user   
        try:
            endusers = current_user.enduser
        except:
            pass
        if endusers:
            return render(request, 'index_enduser.html')

        return redirect('users:home')

def employee_registrationview(request):
    register_url = reverse('users:employee_registration')
    if request.method=='POST':
        register_form =EmployeeForm(data= request.POST)

        if register_form.is_valid():
            register_form.cleaned_data.pop('confirm_password')
            item = Employee(**register_form.cleaned_data)
            item.panchayath_name = request.user.panchayath
            item.save()
            item.set_password(item.password)
            item.save()
            messages.success(request, 'successfully created an account')
            return redirect('users:index')
        else:
            return render(request, 'registration.html', {'register_form':register_form, 'register_url':register_url})
    
    else:
        register_form = EmployeeForm()
        return render(request, 'registration.html', {'register_form':register_form, 'register_url':register_url})


def panchayath_registrationview(request):
    register_url = reverse('users:panchayath_registration')
    if request.method=='POST':
        register_form =PanchayathForm(data= request.POST)

        if register_form.is_valid():
            register_form.cleaned_data.pop('confirm_password')
            item = register_form.save()
            item.set_password(item.password)
            item.save()
            messages.success(request, 'successfully created a pachayath account')
            return redirect('users:index')
        else:
            return render(request, 'registration.html', {'register_form':register_form, 'register_url':register_url})
    
    else:
        register_form = PanchayathForm()
        return render(request, 'registration.html', {'register_form':register_form, 'register_url':register_url})


def enduser_registrationview(request):
    register_url = reverse('users:enduser_registration')
    if request.method=='POST':
        register_form =EndUserForm(data= request.POST)

        if register_form.is_valid():
            register_form.cleaned_data.pop('confirm_password')
            item = register_form.save()
            item.set_password(item.password)
            item.save()
            messages.success(request, 'successfully created a enduser account')
            return redirect('users:index')
        else:
            return render(request, 'registration.html', {'register_form':register_form, 'register_url':register_url})
    
    else:
        register_form = EndUserForm()
        return render(request, 'registration.html', {'register_form':register_form, 'register_url':register_url})


def loginview(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
       
        if user:
            if user.is_active:
                
                login(request,user)
                return redirect('users:index')
            else:
                return HttpResponse(request, 'Your account is disabled')

        else:
            messages.error(request, 'Invalid login details')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


@login_required
def logoutview(request):
    logout(request)

    return redirect('users:home')


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'

    def get_queryset(self):
        current_user = self.request.user
        panchayath = current_user.panchayath
        return Employee.objects.filter(Q(panchayath_name = panchayath)) 


def addnews(request):
    register_url = reverse('users:add_news')
    if request.method=='POST':
        print(request.POST)
        register_form =NewsForm(data= request.POST)

        if register_form.is_valid():
            item = News(**register_form.cleaned_data)
            item.panchayath_name = request.user.panchayath
            item.save()
            messages.success(request, 'successfully created a news!')
            return redirect('users:index')
        else:
            return render(request, 'registration.html', {'register_form':register_form, 'register_url':register_url})
    
    else:
        register_form = NewsForm()
        return render(request, 'registration.html', {'register_form':register_form, 'register_url':register_url})


class ViewNews(ListView):
    model = News
    template_name = 'news_details.html'


    def get_queryset(self):
        current_user = self.request.user
        panchayath = current_user.panchayath
        return News.objects.filter(Q(panchayath_name = panchayath)) 


def salary_updation_view(request, employee_id):
    register_url = reverse('users:update_salary', kwargs={'employee_id':employee_id})
    employee = Employee.objects.get(id= employee_id)
    if request.method == 'POST':
        register_form = SalaryForm(data=request.POST)
        if register_form.is_valid():
            item = Salary(**register_form.cleaned_data)
            item.panchayath_name = request.user.panchayath
            item.employee_name = employee
            item.save()

            return redirect('users:index')

        else:
            return render(request, 'registration.html', {'register_form':register_form, 'register_url':register_url})
    
    else:
        register_form = SalaryForm()
        return render(request, 'registration.html', {'register_form':register_form, 'register_url':register_url})













