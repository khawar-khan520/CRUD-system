from multiprocessing import context
from django.shortcuts import redirect, render, HttpResponse # redirct and 
from django.contrib import  messages
from django.contrib.auth.models import User #
from django.contrib.auth import authenticate,login,logout # from other
from django.contrib.auth.decorators import login_required #
from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def Home(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        form.save()
        form=EmployeeForm()
    
    data=Employee.objects.all()

    context={
        'form':form,
        'data':data,
    }
    
    return render(request,'app1/index.html',context)
    return redirect('login')

# here is login overview 

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('name')
        password=request.POST.get('password')

        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exists')

        user=authenticate(request, username=username, password =password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Incorrect username or password.')
        return render(request, 'app1/login.html')

    return render(request, 'app1/login.html')


""" def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('name')
        pass1=request.POST.get('password')

        try:
            user= user.objects.gets(username=username)
        except:
            messages.error(request, 'user does not exists')

        user=authenticate(request,username=username,password=pass1)

        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

       
    return render (request,'app1/login.html')  """

# Delete View
@login_required(login_url='login')
def Delete_record(request,id):
    a=Employee.objects.get(pk=id)
    return redirect('login')
    a.delete()
    
    

# Update View
@login_required(login_url='login')
def Update_Record(request,id):
    if request.method=='POST':
        data=Employee.objects.get(pk=id)
        form=EmployeeForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:

        data=Employee.objects.get(pk=id)
        form=EmployeeForm(instance=data)
    context={
        'form':form,
    }
    return render (request,'app1/update.html',context)

def view_attendance(request):

    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'app1/view_attendance.html', context)

def mark_attendance_present(request, id):
    employee = Employee.objects.get(id=pk)
    employee.attendance = 'Present'
    employee.save()
    return redirect('view_attendance')

    