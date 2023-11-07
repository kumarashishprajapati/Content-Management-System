from django.shortcuts import render,redirect,HttpResponse
from django.shortcuts import render, get_object_or_404
from.models import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def home(request): # home - page
    return render(request,"index.html")


def profile_view(request): # File Read method
    profile=Article.objects.all()
    query=""
    if "search" in request.POST:
        query=request.POST.get("searchquery")
        profile=Article.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(tags__icontains=query))
    context={"profile":profile,"query":query}
    return render(request, 'profile.html', context=context)


def create_profile(request):   # That is Creat method
    if request.method == "POST":
        author=request.user
        title=request.POST.get("title")
        content=request.POST.get("content")
        publication_date=request.POST.get("publication_date")
        tags=request.POST.get("tags")
        profile_picture=request.FILES.get("profile_picture")

        Article.objects.create(author=author,title=title,content=content,publication_date=publication_date,tags=tags,profile_picture=profile_picture)
        return redirect('profile')
    return render(request,"create.html")



def update_profile(request,pk):  # update file from here
    update_article=Article.objects.get(id=pk)
    if request.method=="POST":
        # update_article.author=request.POST.get("author")
        update_article.title=request.POST.get("title")
        update_article.content=request.POST.get("content")
        # update_article.publication_date=request.POST.get("publication_date")
        update_article.tags=request.POST.get("tags")
        # update_article.profile_picture=request.FILES.get("profile_picture")
        update_article.save()
        return redirect('profile')
    context={'update_article':update_article}
    return render(request,'update.html',context=context)


def signup(request):  # User register method
    if request.method =="POST":
        name=request.POST.get("username")
        Email=request.POST.get("email")
        Password1=request.POST.get("password1")
        Password2=request.POST.get("password2")
        if Password1!=Password2:
            return HttpResponse("Your password are not matched")
        else:
            data=User.objects.create_user(name,Email,Password1)
            data.save()
            messages.success(request,"User added Successfully")
            return redirect('login')
    return render(request,"signup.html")


def login_request(request):  # login method 
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.error(request,'invalid username')
        user=authenticate(request,username=username,password=password)
        if user is None:
            messages.error(request,'invalid password')
            return redirect('login')
        else:
            login(request,user)
            return redirect("profile")  
    return render (request,'login.html')


def logout_request(request): # logout method
    logout(request)
    return redirect('login')