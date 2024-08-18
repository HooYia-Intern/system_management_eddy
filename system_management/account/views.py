from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                messages.error(request, "credentials didn't matched")
            else:
               auth_login(request, user)
               messages.success(request, "login successfull")
               return redirect('/')
    return render(request, 'account/login.html')

def signup(request):
    if request.method == 'POST':
      name = request.POST.get('name', '')
      email = request.POST.get('email', '')
      password1 = request.POST.get('password1', '')
      password2 = request.POST.get('password2', '')

      if name and email and password1 and password2:
        user = User.objects.create_user(name, email, password1)

        print('user created')

        return redirect('/login/')
      else:
         print('something went wrong')
    else:
       print('just show the form')

    return render(request, 'account/signup.html')
