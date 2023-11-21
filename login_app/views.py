from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
# username : hemil password : HEMIL$$$***000
# Create your views here.
def index(request):
     print(request.user)
     if request.user.is_anonymous:
          return redirect('/login')
     return render(request,'index.html')

def login_user(request):
     if request.method=="POST":
          username = request.POST.get('username')
          password = request.POST.get('password')
          print(username,password)
          user = authenticate(username=username, password=password)
          if user is not None:
          # A backend authenticated the credentials
               login(request, user)
               return redirect('/home/')
          else:
               return render(request,'login.html')
    # No backend authenticated the credentials
    
     return render(request,'login.html')

def logout_user(request):
     logout(request)
     return redirect('/login')