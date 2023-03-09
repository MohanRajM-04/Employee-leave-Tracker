from django.contrib import admin
from app1.models import Employee, holiday, Employee_leave

# Register your models here.

admin.site.register(Employee)
admin.site.register(holiday)
admin.site.register(Employee_leave)