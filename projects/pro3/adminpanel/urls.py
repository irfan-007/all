from django.urls import path
from . import views

urlpatterns = [
path('', views.index ,name='index'),
path('index/', views.index ,name='index'),
path('charts/', views.charts ,name='charts'),
path('icons/', views.icons ,name='icons'),
path('login/', views.login ,name='login'),
path('maps/', views.maps ,name='maps'),
path('notifications/', views.notifications ,name='notifications'),
path('tables/', views.tables ,name='tables'),
path('typography/', views.typography ,name='typography'),
path('users/', views.users ,name='users'),
path('add_user/', views.add_user ,name='add_user'),
path('delete_user/<int:id>/', views.delete_user ,name='delete_user'),
path('update_user/<int:id>/', views.update_user ,name='update_user'),
path('update_link/<int:id>/', views.update_link ,name='update_link'),
]