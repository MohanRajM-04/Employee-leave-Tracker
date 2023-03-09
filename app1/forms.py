from django.forms import ModelForm
from app1.models import Employee_leave, Employee



class Employee_leave_form(ModelForm):
    class Meta:
        model = Employee_leave

        fields = ['date','reason']

class update_emp_details(ModelForm):
    class Meta:
        model = Employee
        fields = ['age','gender', 'email', 'department','company_name','leave_available']











