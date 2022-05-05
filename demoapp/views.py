from django.shortcuts import render, HttpResponse
from . models import *
import base64

# Create your views here.
def newfunction(request):
    return render(request,'index.html') 

def login(request):
    try:
        if request.method == "POST":            
            email = request.POST['email']
            password1=request.POST['password']
            password2=password1.encode("utf-8")
            password=base64.b64encode(password2)
            # password=request.POST['password']
            print(password)
            ob1 = usertable.objects.get(email=email)
            if ob1.password==password:
                request.session['sample'] = ob1.id
                return render(request,'home.html')


    except Exception as e:
        print(e)
    return render(request,'index.html',{"msg1": "invalid username or password"})

def register(request):
    return render(request,'register.html')   

def registersuc(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            obj = usertable.objects.filter(username=username).exists()
            if(obj == False):
                username = request.POST['username']
                email = request.POST['email']
                dob = request.POST['dob']
                phonenum=request.POST['phone']
                password1=request.POST['password']
                password2=password1.encode("utf-8")
                password=base64.b64encode(password2)
                gender=request.POST['gender']
                obj1 = usertable(username=username, email=email,dob=dob, phone_num=phonenum, password=password, gender=gender)
                obj1.save()
                return render(request, 'register.html', {"msg": "saved successfully"})
            else:
                return render(request, 'register.html', {"err": "user already exists"})
    except Exception as e:
        print(e)
    return render(request,'register.html', {"msg":'error'})       