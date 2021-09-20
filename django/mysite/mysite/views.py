from django.shortcuts import render
from django.http import HttpResponse

def hello_world(requests):
	return HttpResponse("Hello intership. i'm coming to get you.")

def login_page(requests):
   return render(requests, 'login.html')

def signup_page(requests):
   return render(requests, 'signup.html')
