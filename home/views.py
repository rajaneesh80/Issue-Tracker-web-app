from django.shortcuts import render

from django.shortcuts import render

from django.http import HttpResponse

# def home(request):
# 	return HttpResponse("Helllo from Issue_Bug!!")

def home(request):
	return render(request, 'home.html')

