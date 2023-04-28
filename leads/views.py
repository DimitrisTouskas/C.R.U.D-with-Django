import email
from email import message
from importlib.resources import contents
from multiprocessing import context
from pickle import NONE
from turtle import title
from unicodedata import name
from urllib import response
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.templatetags.static import static
from django.test import tag
from .models import Students
from .models import Blospost
from .forms import PostForm, RegisterForm, StudentsForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
# from django.contrib.sessions.models import Sessions
# from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Δουλευει


@login_required(login_url="/login")
def addStudents(request):
    form = StudentsForm()
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "addStudents.html", {"form": form})


@login_required(login_url="/login")
def editStudents(request, id):
    student = Students.objects.get(pk=id)
    editform = StudentsForm(request.POST or None, instance=student)

    if editform.is_valid():
        editform.save()
        return redirect("/foitites", {"editform": editform})
    return render(request, "editStudents.html", {"editform": editform})


@login_required(login_url="/login")
def editPosts(request, id):
    student = Blospost.objects.get(pk=id)
    postform = PostForm(request.POST or None, instance=student)

    if postform.is_valid():
        postform.save()
        return redirect("posts")
    return render(request, "editPosts.html", {"postform": postform})


# Δουλευει
def delete(request, id):
    foititis = get_object_or_404(Students, pk=id)
    foititis.delete()
    return redirect("/foitites")


# Δουλευει
@login_required(login_url="/login")
def delete_posts(request, id):
    post = get_object_or_404(Blospost, pk=id)
    post.delete()
    return redirect("posts")


# Δουλευει
@login_required(login_url="/login")
def foitites(request):
    row = Students.objects.all()
    stu = {
        "student_number": row
    }

    return render(request, 'foitites.html', stu)


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect('posts')

    else:
        return render(request, "registration/login.html")
    return render(request, "registration/login.html")


@login_required(login_url="/login")
def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('login')


# Δουλευει
@login_required(login_url="/login")
def posts(request):
    form = PostForm(instance=request.user)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        tag = request.POST.get("tag")
        date_posted = request.POST.get("date_posted")

        if request.user.id is not None:
            post = Blospost.objects.create(
                title=title, content=content, tag=tag, date_posted=date_posted, user_id=request.user.id)
        else:
            return redirect("login")
    row = Blospost.objects.all()
    context = {
        "post_number": row,

    }
    return render(request, "posts.html", context)


def profile():
    return


@login_required(login_url="/login")
def search(request):
    if request.method == 'POST':
        searched = request.POST["searched"]
        DBBlog = Blospost.objects.filter(
            Q(title__contains=searched) | Q(
                tag__contains=searched) | Q(content__contains=searched))
        DBStudents = Students.objects.filter(Q(name__contains=searched) | Q(lastname__contains=searched) | Q(email__contains=searched) | Q(
            dieuthinsi__contains=searched) | Q(phone__contains=searched) | Q(eksamino__contains=searched) | Q(A_M__contains=searched))

        return render(request, 'search.html', {'searched': searched, 'DBBlog': DBBlog, 'DBStudents': DBStudents})
    else:
        return render(request, 'search.html')


def signup(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "foitites.html", {"form": form})
    return render(request, "signup.html", {"form": form})


def home(request):

    return render(request, 'index.html')
