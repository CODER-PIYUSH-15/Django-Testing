from django.shortcuts import render,redirect
from xyz.models import *
from xyz.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def home(request):
    s=Student.objects.all()
    data={
        'student': s
    }
    return render(request, "index.html", data)

def signup(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    else:
        if request.method == "POST":
            form=SignUpForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                except Exception as e:
                    print(e)
        form=SignUpForm()
        data={
            "form":form
        }
        return render(request, "signup.html", data)

def signin(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    else:
        if request.method == "POST":
            form=SignInForm(request=request, data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return redirect('/profile')
        form=SignInForm()
        data={
            "form":form
        }
        return render(request,"signup.html", data)

@login_required(login_url='/signin')
def profile(request):
    if request.method == "POST":
        email=request.POST.get("email")
        first_name=request.POST.get("firstname")
        last_name=request.POST.get("lastname")
        print(email,first_name, last_name)
        u=User.objects.get(username=request.user.username)
        u.first_name=first_name
        u.last_name=last_name
        u.email=email
        u.save()
        return redirect("/profile")
    return render(request, "profile.html")


def signout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/signin')
def delete(request,id):
    s=Student.objects.get(sid=id)
    s.delete()
    return redirect('/')