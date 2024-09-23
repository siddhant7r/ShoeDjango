from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def rpage(request):
    return render(request,'registration.html')

def register(request):
    print(request.POST)
    cstoken=request.POST.get('csrfmiddlewaretoken')
    name=request.POST.get('nm')
    email=request.POST.get('em')
    age=request.POST.get('age')
    contact=request.POST.get('con')
    password=request.POST.get('pass')

    response=render(request,'login.html')
    response.set_cookie('name',name)
    response.set_cookie('email',email)
    response.set_cookie('age',age)
    response.set_cookie('contact',contact)
    response.set_cookie('password',password)
    return response

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        name1=request.COOKIES['name']
        contact1=request.COOKIES['contact']
        email1=request.COOKIES['email']
        password1=request.COOKIES['password']
        if email==email1:
            if password==password1:
                data={
                'name':name1,
                'email':email1,
                'contact':contact1,
                'password':password1
                }
                return render(request,'welcome.html',data)
            else:
                msg="Email and Password not matching"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="Email Not registered" 
           
            return render(request,'login.html',{'msg':msg})   
           
    else:
        msg=""
        return render(request,'login.html',{'msg':msg})

def delete(request):
    response=render(request,'home.html')
    response.delete_cookie('name')
    response.delete_cookie('email')
    response.delete_cookie('contact')
    response.delete_cookie('age')
    response.delete_cookie('password')
    return response

