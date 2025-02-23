from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.models import User, auth

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("Login successful")
            return redirect('/')
        else:
                messages.info(request, 'Invalid credentials')
                return redirect('register')
    else:
        return render(request, 'register.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"Email taken")
                 return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                auth.login(request, user)
                messages.info(request,"Registration Succesfull..")
                return redirect('/')
        else:
            messages.info(request,"Password don't match")
            return redirect('register')
    else:
        return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    print('logout successful')
    return redirect('/')
