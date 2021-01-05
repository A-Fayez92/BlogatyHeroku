from django.shortcuts import render, redirect
from .models import userBlogs
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from .forms import BlogForm , CreateUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request , username=username , password=password)

        if user is not None :
            login(request,user)
            return redirect('home')

    return render(request,'login.html') 

def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request,'signup.html', context)  
@login_required(login_url='login')
def home(request):
    all_blogs = userBlogs.objects.filter(author=request.user.id)

    context = {
        'all_blogs':all_blogs
    }

    return render(request,'home.html', context)

@login_required(login_url='login')
def deleteBlog(request, pk):
    blog = userBlogs.objects.get(id=pk)
    if request.method == "POST":
        blog.delete()
        return redirect('home')
    context = {
        'blog':blog
    }
    return render(request, 'deleteBlog.html' ,context)

@login_required(login_url='login')
def CreateBlog(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form' : form
    }
    return render(request,'blogForm.html',context)

@login_required(login_url='login')
def EditBlog(request,pk):
    blog = userBlogs.objects.get(id=pk)
    
    if request.method == "POST":
        form = BlogForm(request.POST , instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = BlogForm(instance=blog)
    context = {
        'form' : form
    }
    return render(request, 'blogForm.html',context)

@login_required(login_url='login')
def ViewBlog(request, pk):
    blog = userBlogs.objects.get(id=pk)
    context = {
        'blog' : blog
    }
    return render(request, 'ViewBlog.html', context)

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')