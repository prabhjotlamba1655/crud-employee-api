from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import  Employee

# Create your views here.

#On the basis tf the request employee_list function change the current page employee register page to employee list page  
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)

# employee_form check the details enter in the from is valid or not, If not error then it shows the error 
# otherwise it stores the data in the database
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/list')

# To perform deletetion operations 
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')
