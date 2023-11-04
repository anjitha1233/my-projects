from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import render, redirect, get_object_or_404



# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']

        password=request.POST['password']
        user=auth.authenticate(username=username , password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credential')
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
            else:
                 user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
                 user.save
                 print("user created")
                 return redirect('login')
        else:
            print("not matched")
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')