from django.shortcuts import render
from issue.models import Issue

def searchResult(request):
    issues = Issue.objects.filter(name__icontains=request.GET['q'])
    return render(request, "issues.html", {"issues": issues})
