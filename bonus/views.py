from django.shortcuts import render

from django.http import HttpResponse

from .models import User

def index(request):
    userList = User.objects.all()

    return render(
        request,
        'bonus/index.html',
        context = {'user_list': userList})

def addSuggest(request):
    userList = User.objects.all()

    return render(
        request,
        'bonus/addSuggest.html',
        context = {'user_list': userList})


