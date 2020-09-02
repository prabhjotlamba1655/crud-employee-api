from django.contrib import admin
from employee_register import models

# Register your models here.
admin.site.register([
    models.Employee,
    models.Position
])