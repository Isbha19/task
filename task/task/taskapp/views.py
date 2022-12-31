from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,'index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('taskapp:button')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('taskapp:login')
    return render(request, "login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['confirmpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('taskapp:register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                print("user created")
                return redirect('taskapp:login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('taskapp:register')
    return render(request,"register.html")
#
def form(request):
    if request.method=='POST':
        name=request.POST['name']
        dob=request.POST['dob']
        return redirect('taskapp:final')
    return render(request,'form.html')
def button(request):
    return render(request,'button.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def final(request):
    return render(request,'final.html')