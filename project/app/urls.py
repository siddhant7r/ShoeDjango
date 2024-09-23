from . import views
from django.urls import path
urlpatterns=[
    path('',views.home,name='home'),
    path('registrationpage',views.rpage,name='rpage'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('delete',views.delete,name='delete'),
]