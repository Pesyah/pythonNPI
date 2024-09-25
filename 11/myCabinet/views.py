from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

user = authenticate(username="john", password="secret")
if user is not None:
    # A backend authenticated the credentials
    ...
else:
    # No backend authenticated the credentials
    ...


def login(request):
    if request == 1:
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    print(request.method)
    return render(request, 'login.html')