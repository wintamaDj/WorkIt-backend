from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Oops... Something went wrong, and you shouldn't be seeing this page! Please contact support or an admin")