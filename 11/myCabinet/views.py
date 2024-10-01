from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import json
from django.http import HttpResponse

def loginRequest(request):
    if request.method == "POST":
        body = json.loads(request.body)
        username = body["username"]
        password = body["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('')
        return HttpResponse(status=401)
    if request.method == "GET":
        return render(request, 'login.html')
    
def registration(request):
    if request.method == "POST":
        body = json.loads(request.body)
        username = body["username"]
        password = body["password"]
        user = User.objects.get(username=username)
        if user:
            return render(request, 'registration.html', {"alert": """alert("Такой пользователь уже существует")"""})
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('/cabinet')
    if request.method == "GET":
        return render(request, 'registration.html')