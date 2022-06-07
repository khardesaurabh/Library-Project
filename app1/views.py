from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.sessions.models import Session
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request,"option.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            request.session['is_logged'] = True
            user = request.user.username
            request.session["username"] = user
            messages.success(request,"Logged in")
            response = redirect('index')
            response.set_cookie('username',username)
            response.set_cookie('login_status',True)
            return response
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,"login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('login')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('login')
            else:
                user = User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,password=password2)
                user.save()
                messages.success(request,'Registered Successfully')
                return redirect('login')
        else:
            messages.warning(request,"Passwords dont match")
    return render(request,"signup.html")



def logout(request):
    auth.logout(request)
    response = redirect('home')
    response.delete_cookie('username')
    response.delete_cookie('login_status')
    return response

def index(request):
    if request.session.has_key('username'):
        return render(request,'index.html')
    else:
        messages.info(request,"Please login to continue")
        return redirect('login')

def addbook(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            book_name = request.POST.get("book_name")
            author_name = request.POST.get("author_name")
            edition = request.POST.get("edition")
            genre = request.POST.get("genre")
            newbook = Book.objects.create(book_name=book_name,author_name=author_name,edition=edition,genre=genre)
            newbook.save()
            messages.success(request,"Book Added Successfully")
            return redirect('displaybooks')
        return render(request,'addbook.html')
    else:
        messages.info(request,"Please login to continue")
        return redirect('login')

def displaybooks(request):
    if request.session.has_key('username'):
        allbooks = Book.objects.all()
        return render(request,"display.html",{'allbooks':allbooks})
    else:
        messages.info(request,"Please login to continue")
        return redirect('login')

def deletebook(request,id):
    if request.session.has_key('username'):
        book = Book.objects.get(pk=id)
        book.delete()
        messages.success(request,"Book Deleted")
        return redirect('displaybooks')
    else:
        messages.info(request,"Please login to continue")
        return redirect('login')

def updatebook(request,id):
    if request.session.has_key('username'):
        book = Book.objects.get(id=id)
        form = Bookform()
        if request.method == "POST":
            form = Bookform(request.POST, instance=book)
            if form.is_valid():
                form.save()
                messages.success(request,"Book Updated")
                return redirect("displaybooks")
        else:
            book = Book.objects.get(id=id)
            form = Bookform(instance=book)
            context = {'form' : form}
            return render(request,"updatebook.html", context)
    else:
        messages.info(request,"Please login to continue")
        return redirect('login')

def searchbook(request):
    if request.session.has_key('username'):
        search = request.POST.get("search")
        book = Book.objects.filter(book_name=search) or Book.objects.filter(author_name=search) or Book.objects.filter(genre=search)
        if book is not None:
            return render(request,"search.html",{'book':book})
        else:
            messages.error(request,"No match found")
            return redirect('index')
    else:
        messages.warning(request,"Please login to continue")
        return redirect('login')

def displayusers(request):
    if request.session.has_key('username'):
        users = User.objects.all()
        return render(request,"displayusers.html",{'users':users})
    else:
        messages.warning(request,"Please login to continue")
        return redirect('login')


def contact(request):
    if request.session.has_key('username'):
        return render(request,"contact.html")
    else:
        messages.warning(request,"Please login to continue")
        return redirect('login') 




