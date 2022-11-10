from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *


def page_404(request):
    return render(request, 'page-404.html')


@login_required(login_url='sign-in')
def dashboard_view(request):
    context = {
    }
    return render(request, 'dashboard.html', context)


def sign_in(request):
    return render(request, 'login.html')


def for_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.count() > 0:
            usr = authenticate(username=username, password=password)
            if usr.status == 1:
                if usr is not None:
                    login(request, usr)
                    return redirect('dashboard')
                else:
                    return redirect('sign-in')
            return redirect('sign-in')
        else:
            return redirect('sign-in')
    else:
        return redirect('sign-in')


def logout_view(request):
    logout(request)
    return redirect('sign-in')


@login_required(login_url='sign-in')
def reset(request):
    user = request.user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_password = request.POST.get('new-password')
        prove = request.POST.get('confirm-password')
        usr = authenticate(username=user.username, password=password)
        if new_password == prove:
            usr.username = username
            usr.set_password(new_password)
            usr.save()
            return redirect('dashboard')
        return redirect('reset')
    return render(request, 'reset-password.html', {'admin': user})


@login_required(login_url='sign-in')
def about_view(request):
    return render(request, 'about.html', {'about': About.objects.all()})


def add_about(request):
    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES.get("image")
        text = request.POST.get("text")
        About.objects.create(
            title=title,
            image=image,
            text=text,
        )
    return redirect("about")


def update_about(request, pk):
    about = About.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        image = request.POST.get('image')
        about.title = title
        about.text = text
        if image is None:
            about.image = image.image
        else:
            about.image = image
        about.save()
        return redirect('about')
    return render(request, 'update-about.html', {'about': About.objects.get(id=pk)})


def delete_about(request, pk):
    about = About.objects.get(id=pk)
    about.delete()
    return redirect('about')
