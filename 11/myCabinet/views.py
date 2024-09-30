from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import json

def loginRequest(request):
    if request.method == "POST":
        print(request.POST)
        body = json.loads(request.body)
        username = body["username"]
        password = body["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('')
        return render(request, 'login.html', {"alert": """alert("неверный логин или пароль")"""})
    if request.method == "GET":
        return render(request, 'login.html')