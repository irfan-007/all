from django.shortcuts import render
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

    return render(request,'admin/users.html',{'users':users})








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
