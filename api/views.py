from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import json

def auth(request):
    if(request.method == 'POST'):
        data = json.loads(request.body)
        username = data["username"]
        password = data["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"authStatus": "success"})
        else:
            return JsonResponse({"authStatus": "failed", "message": "Invalid login details"})

def register(request):

    if(request.method == 'POST'):
        data = json.loads(request.body)
        username = data["username"]
        email = data["email"]
        password = data["password"]

        r = User.objects.filter(username=username)
        if r.count():
            return JsonResponse({"saveStatus": "failed", "message": "Username already exists"})
        
        r = User.objects.filter(email=email)
        if r.count():
            return JsonResponse({"saveStatus": "failed", "message": "Email already exists"})

        user = User.objects.create_user(username, email, password)
        user.save()

        return JsonResponse({"saveStatus": "success"})

def chart(request):

    data = [
        {"name": "Nitrogen", "value": 40},
        {"name": "Phosphorous", "value": 20},
        {"name": "Sediment", "value": 30},
        {"name": "Chlorin", "value": 10},
    ]

    return JsonResponse(data, safe=False)

def home(request):
    return HttpResponse("Welcome to api service")
