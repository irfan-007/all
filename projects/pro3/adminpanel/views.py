from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from accounts.models import User_details

# Create your views here.

def index(request):
    return render(request,'admin/index.html')

def users(request):

    users=User.objects.all()
    for user in users:
        temp=User_details.objects.filter(user=user).first()
        user.phone=temp.phone

    return render(request,'admin/users.html',{'users':users ,'flag':0})

def add_user(request):
    if request.method=='POST':
    
        phone=request.POST['phone']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
         
        user=User.objects.create_user(username=email,first_name=fname,last_name=lname,password=password,email=email)
        User_details.objects.create(phone=phone,user=user)

        return redirect(users)
    
def delete_user(request,id):
    user=User.objects.get(pk=id)
    user.delete()

    return redirect(users)

def update_user(request,id):
    if request.method=='POST':
        phone=request.POST['phone']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']

        user=User.objects.get(pk=id)
        temp=User_details.objects.get(pk=id)
        temp.phone=phone
        user.fname=fname
        user.lname=lname
        user.email=email
        user.password=password
        user.save()
    
    return redirect(users)

def update_link(request,id):
    return render(request,'admin/users.html',{'id':id ,'flag':1})




def charts(request):
    return render(request,'admin/charts.html')

def icons(request):
    return render(request,'admin/icons.html')

def login(request):
    return render(request,'admin/login.html')

def maps(request):
    return render(request,'admin/maps.html')

def notifications(request):
    return render(request,'admin/notifications.html')

def tables(request):
    return render(request,'admin/tables.html')

def typography(request):
    return render(request,'admin/typography.html')
