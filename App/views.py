from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from App.models import Student

# Create your views here.
def home(request):
    user=request,User
    students=Student.objects.all()
  
    return render(request,"home.html",{'username':user,'students':students})

def signupPage(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        pass1=request.POST.get("password")
        pass2=request.POST.get("password2")
        if pass1==pass2:
            Myuser = User.objects.create_user(name,email,pass1)
            Myuser.save()
            return redirect("loginpage")
        else:
            return redirect("signupage")
    return render(request,"signup.html")

def loginPage(request):
    if request.method == "POST":
        name=request.POST.get("name")
        password=request.POST.get("password")
        user = authenticate(username=name,password=password)
        if user is not None:
            return redirect("homepage")
        else:
            return redirect("loginpage")

    
    return render(request,"login.html")
def addPage(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        semester=request.POST.get("semester")
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        batch=request.POST.get("batch")

        students=Student(
            name=name,
            email=email,
            semester=semester,
            address=address,
            phone=phone,
            batch=batch
        )
        students.save()
        return redirect("homepage")
    return render(request,"home.html")

def editPage(request):
    students=Student.objects.all()
    return render(request,"home.html",students)


def updatepage(request,id):
   
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        semester=request.POST.get("semester")
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        batch=request.POST.get("batch")

        students=Student(
            id=id,
            name=name,
            email=email,
            semester=semester,
            address=address,
            phone=phone,
            batch=batch,
        )
        students.save()
        return redirect("homepage")
    return render(request,"home.html")

def deletePage(request,id):
    students=Student.objects.get(id=id)
    students.delete()
    return render(request,"home.html")
   
