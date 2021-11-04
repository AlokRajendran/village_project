from django.urls import path
from .views import (HomeView, index,loginview, employee_registrationview, panchayath_registrationview, enduser_registrationview, logoutview,
 complaint_registrationview,news_registrationview, salary_registrationview)
app_name = 'users'

urlpatterns = [
    path('',HomeView.as_view(), name= 'home'),
    path('login/',loginview, name= 'login'),
    path('logout/',logoutview, name= 'logout'),

    path('employee-registration/',employee_registrationview, name= 'employee_registration'),
    path('panchayath-registration/',panchayath_registrationview, name= 'panchayath_registration'),
    path('user-registration/',enduser_registrationview, name= 'enduser_registration'),
    
    path('home/',index, name= 'index'),

    path('salary-registration/', salary_registrationview, name= 'salary_registration'),
    path('news-registration/', news_registrationview, name= 'news_registration'),
    path('complaint-registration/', complaint_registrationview, name= 'complaint_registration'),



    
]
