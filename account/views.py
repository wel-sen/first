from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views import View



# Create your views here.

class Register(View):
    def get(self,request,*args,**kwargs):
        
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            
            if password==confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"username exists")
                    return redirect('/register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"email exists")
                    return redirect('/register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.info(request,"user added")
                    return redirect('/login')
            else:
                messages.info(request, "password doesn't much")
                return redirect('/register')
        else:
            
            return render(request, 'register.html')
        return redirect('/')
    
class Login(View):
    def get(self,request,*args,**kwargs):
        
        if request.method == "POST":
            username=request.POST['username']
            password=request.POST['password']
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.info(request,'Invalid Credentials')
        else:
            return render(request,'login.html')
        

            
        
