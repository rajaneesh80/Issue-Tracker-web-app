from django.shortcuts import render

from django.shortcuts import render

from django.http import HttpResponse

# def home(request):
# 	return HttpResponse("Helllo from Issue_Bug!!")

def home(request):
	''' View for home page'''
	return render(request, 'home.html')

