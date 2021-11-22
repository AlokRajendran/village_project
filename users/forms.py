from django.db.models import fields
from . models import Employee, Panchayath, EndUser, Complaint, News, Salary
from django import forms


class EmployeeForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())
    confirm_password = forms.CharField(widget= forms.PasswordInput())

    class Meta:
        model = Employee
        fields = ('email','password', 'employee_name', 'job_title', 'address', 'phone') 


    def clean(self):
        cleaned_data = super(EmployeeForm,self).clean()
        #clean()is  used to clear data from form after submission
        
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('password doesnt match')


class PanchayathForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())
    confirm_password = forms.CharField(widget= forms.PasswordInput())

    class Meta:
        model = Panchayath
        fields = ('email', 'password', 'panchayath_name', 'country', 'state', 'district', 'pincode')
        

    def clean(self):
        cleaned_data = super(PanchayathForm,self).clean()
        #clean()is  used to clear data from form after submission
        
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('password doesnt match')


class EndUserForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())
    confirm_password = forms.CharField(widget= forms.PasswordInput())
    panchayath_name = forms.ModelChoiceField(queryset=Panchayath.objects.all())


    class Meta:
        model = EndUser
        fields = ('panchayath_name', 'email','password', 'enduser_name', 'job_title', 'address', 'phone') 
        

    def clean(self):
        cleaned_data = super(EndUserForm,self).clean()
        #clean()is  used to clear data from form after submission
        
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('password doesnt match')


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('description',)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title','description',)


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ('salary','ta','da','credited_on')
