from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *

# Create your views here.

def index(request):

    return render(request,'store/index.html')

def signup(request):
    if request.method=='POST':
    
        phone=request.POST['phone']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
         
        if User.objects.filter(email=email).exists():
            return JsonResponse(
                {'success':False , 'emailerror':True},
                safe=False
            )

        else:
            user=User.objects.create_user(username=email,first_name=fname,last_name=lname,password=password,email=email)
            User_details.objects.create(phone=phone,user=user)
            
            print('user created')
            return JsonResponse(
                {'success':True},
                safe=False
            )
    else:
        return render(request,'accounts/signup.html')



def login(request):
    print('0000#############777777777777777777777')
    #if 'email' in request.session:
    if request.user.is_authenticated:
        return redirect(index)

    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(username=email,password=password)

        if user is not None:
            print('0000#############')
            auth.login(request,user)
            print('0000##########333')

            #request.session['email']=email
            return redirect(index)
        else:
            messages.info(request,'invalid credentials')
            print('0000#############gggg')
            
            return redirect(login)
            
    else:
        
        return render(request,'accounts/login.html')



def logout(request):
    #if 'email' in request.session:
    if request.user.is_authenticated:
        #request.session.flush()
        auth.logout(request)
        
    return redirect(login)