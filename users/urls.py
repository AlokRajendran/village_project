from django.urls import path
from .views import HomeView,EmployeeListView, index,loginview, employee_registrationview, panchayath_registrationview, enduser_registrationview, logoutview, addnews,ViewNews, salary_updation_view

app_name = 'users'

urlpatterns = [
    path('',HomeView.as_view(), name= 'home'),
    path('login/',loginview, name= 'login'),
    path('logout/',logoutview, name= 'logout'),

    path('employee-registration/',employee_registrationview, name= 'employee_registration'),
    path('panchayath-registration/',panchayath_registrationview, name= 'panchayath_registration'),
    path('user-registration/',enduser_registrationview, name= 'enduser_registration'),
    
    path('home/',index, name= 'index'),
    path('employee-list/',EmployeeListView.as_view(), name='employee_list'),

    
    path('add-news/', addnews, name= 'add_news'),

    path('news/', ViewNews.as_view(), name= 'news'),

    path('update-salary/<int:employee_id>', salary_updation_view, name= 'update_salary')


    # path('salary-registration/', salary_registrationview, name= 'salary_registration'),
    # path('complaint-registration/', complaint_registrationview, name= 'complaint_registration'),
  
    
]
