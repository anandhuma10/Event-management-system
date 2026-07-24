from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
# Create your views here.

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')

        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already Taken')
                return redirect('register')
            else:
                user_reg=User.objects.create_user(username=username,email=email,password=password)
                user_reg.save()
                messages.info(request,'Successfully created')
                return redirect('/')
        else:
            messages.info(request,"Password Doesn't match")
            return redirect('register')    

    return render(request,'regi.html')


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/') 
        else:
            return redirect('register')

    return render(request,'log.html')
