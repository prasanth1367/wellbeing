from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
import django.contrib.auth as auth


# Create your views here.
from .models import *


def welcome(request):
    return render(request, 'home/index.html')


def Aboutus(request):
    return render(request, 'home/about-us.html')


def HealthTips(request):
    return render(request, 'home/healthtips.html')


def Blogs(request):
    return render(request, 'home/blog.html')


def Water(request):
    waterobj = Water_list.objects.all()
    return render(request, 'home/water.html', {'lit': waterobj})


def water_ajax(request):
    data = {}
    data['error'] = False
    if request.is_ajax and request.method == "POST":
        dropdownValue = request.POST['dropdownValue']
        value = str(dropdownValue.strip())
        print(value)
        values = Water_list.objects.filter(name=value)
        print(values[0].litres)
        if len(values) is not None:
            data['litres'] = values[0].litres
        else:
            data['error'] = True
        return JsonResponse(data, status=200)
    else:
        return JsonResponse({"error": ""}, status=400)


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/welcome/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please login.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def contact(request):
    if request.method == 'POST':
        con = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        con.name = name
        con.email = email
        con.subject = subject
        con.save()

    return render(request, 'home/contact-us.html')


def logout(request):
    auth.logout(request)
    return redirect('/welcome')


