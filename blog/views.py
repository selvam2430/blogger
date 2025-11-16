from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, Comments
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def test(request):
    return HttpResponse("This is Working") 

def home(request):
    aaa = request.user
    print("current-user",aaa)
    data = Blog.objects.all()
    print(data)
    return render(request, "home.html", {"blogs":data})

def blogDetails(request, pk):
    blogsssss = Blog.objects.get(id=pk)
    comments = Comments.objects.filter(blog=blogsssss)
    print(blogsssss)
    print(comments)
    return render(request, "blog_details.html", {"blog":blogsssss, "comment_data":comments})

def add_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        context = request.POST.get("content") 
        aaa = request.POST.get("author")

       
        Blog.objects.create(
            title = title,
            description = context,
            author = aaa
        )
        return redirect("home")
    return render(request, "add_form.html")
    
def edit_page(request, pk):
    data=Blog.objects.get(id=pk)
    if request.method=="POST":
        print(request.POST.get("_method"))
        if request.POST.get("_method")=="PATCH":
            title = request.POST.get("title")
            print(request.POST.get("title"))
            context = request.POST.get("content")
            aaa = request.POST.get("author")
            if title :
                data.title=title
                data.save()
            if context :
                data.description=context
                data.save()
            if aaa : 
                data.author=aaa
                data.save()
            return redirect("home")
            # return render(request, 'home.html')

    return render(request, 'edit.html', {"form_edit":data})

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
def login_page(request):
    if request.method=="POST":
        name = request.POST.get("user")
        passs = request.POST.get("pass")
        user = authenticate(request, username = name, password=passs)
        login(request,user)
        return redirect("home")
    return render(request,"login.html")
def reg_page(request):
    if request.method == "POST":
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        email = request.POST.get("email")
        passw = request.POST.get("password")
        c_passw = request.POST.get("c_password")
        print(f_name,l_name,email,passw,c_passw)
        if passw == c_passw:
            h_passw = make_password(passw)
            user=User.objects.create(
                first_name = f_name,
                last_name = l_name,
                username = f_name+l_name,
                email = email,
                password = h_passw
            )
            # user.password=make_password(passw)
            # user.save()
            return redirect("login_page")
    return render(request,"register.html")
