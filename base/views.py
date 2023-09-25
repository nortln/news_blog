from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterationForm, AddBlog, AddComment
from .models import New, Comment

def home(request):
    news = New.objects.all().order_by("-date_created")
    form = AddBlog(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    context = {
        "news": news,
        "form": form,
    }
    return render(request, "index.html", context)

@login_required(login_url="login")
def detail(request, pk):
    news = New.objects.get(id=pk)
    new = get_object_or_404(New, pk=pk)
    comments = new.comment_set.all()
    form = AddComment(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.news = new
            form_instance.save()

    
    context = {
        "news": news,
        "comments": comments,
        "form": form,
    }
    return render(request, "detail.html", context)




def add_comment(request, pk):
    return render(request, "detail.html")

def register_user(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterationForm()
    context = {
        "form": form
    }
    return render(request, "register.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login.html", {"error_message": "Login Credentials Invalid"})
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return render(request, "index.html")