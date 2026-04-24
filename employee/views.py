from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .models import Employee

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'home.html', {'error': 'Invalid credentials'})

    return render(request, 'home.html')

# Add Employee View
@login_required
def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        emp_id = request.POST.get('emp_id')
        designation = request.POST.get('designation')
        date_of_joining = request.POST.get('date_of_joining')
        department = request.POST.get('department')
        salary = request.POST.get('salary')
        experience = request.POST.get('experience')

        Employee.objects.create(
            name=name,
            emp_id=emp_id,
            designation=designation,
            date_of_joining=date_of_joining,
            department=department,
            salary=salary,
            experience=experience
        )

    return render(request, 'add_employee.html')



# show the data
@login_required
def view_employees(request):
    employees = Employee.objects.all()
    return render(request, 'view_employees.html', {'employees': employees})



#delete the data
def delete_employee(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('view_employees')


# to display the data
def update_employee(request, id):
    emp = Employee.objects.get(id=id)

    if request.method == 'POST':
        emp.name = request.POST.get('name')
        emp.emp_id = request.POST.get('emp_id')
        emp.designation = request.POST.get('designation')
        emp.date_of_joining = request.POST.get('date_of_joining')
        emp.department = request.POST.get('department')
        emp.salary = request.POST.get('salary')
        emp.experience = request.POST.get('experience')

        emp.save()
        return redirect('view_employees')

    return render(request, 'add_employee.html', {'emp': emp})


def hr_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('view_employees')

    return render(request, 'login.html')

def admin_logout(request):
    logout(request)
    return redirect('home')