import os
import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import Issue, Comment
from .forms import IssueForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


 ############# issue #######################

@login_required   
def my_issues(request):

    """
    Create a view that will return Authenticated user 
    all the Issues render them to the 'myissues.html' template
     
    """

    m_issues = Issue.objects.filter(created_by=request.user).order_by('-created_at')

    # Pagination settings##

    page = request.GET.get('page', 1)
    paginator = Paginator(m_issues, 10)
    
    try:
        m_issues = paginator.page(page)
        
    except PageNotAnInteger:
        
        m_issues = paginator.page(1)
        
    except EmptyPage:
        
        m_issues = paginator.page(paginator.num_pages)

    return render(request, "issue/myissues.html", {'m_issues': m_issues})

################ ###########################
    
@login_required
def all_issues(request):

    """
    Create a view that will return all the Issues render them to the
     'issues.html' template

    """


    allissues = Issue.objects.all().order_by('-created_at')
    comments = Comment.objects.all()

    # Pagination settings ##

    page = request.GET.get('page', 1)
    paginator = Paginator(allissues, 10)
    
    try:
        allissues = paginator.page(page)
        
    except PageNotAnInteger:
        
        allissues = paginator.page(1)
        
    except EmptyPage:
        
        allissues = paginator.page(paginator.num_pages)

    return render(request, 'issue/issues.html', {'issues': allissues}, {'comments': comments})

################ ###########################

@login_required   
def create_issue(request):

    """
    Create a view that allow Authenticated user 
    to create a new issue
     
    """
    if request.method == 'POST':
        form = IssueForm(request.POST,  request.FILES)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.created_by = request.user
            issue.save()
            messages.success(request, 'New issue created successfully!')
            return redirect('my_issues')
    else:
        form = IssueForm()
    return render(request, 'issue/issueform.html', {'form': form})


################ ###########################
    
@login_required      
def edit_issue(request, pk):

    """
    Create a view that allow Authenticated user 
    to edit owm issues
     
    """
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'POST':
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your issue was updated successfully!')
            return redirect(my_issues)
    else:
        form = IssueForm(instance=issue)
    return render(request, 'issue/issueform.html', {'form': form})

################ ###########################

def delete_issue(request, pk):

    """
    Create a view that allow Authenticated user 
    to delete owm issues
     
    """
    issue = get_object_or_404(Issue, pk=pk)
    issue.delete()
    return redirect(my_issues)

################ ###########################

@login_required   
def upvote(request, issue_id):

    """
    Create a view that allow Authenticated user 
    to upvote the issues
     
    """
    if request.method == 'POST':
        issue = get_object_or_404(Issue, pk=issue_id)
        issue.upvotes += 1
        issue.save()
        messages.success(request, 'Upvoted successfully!')
        return redirect('/issue/' +str(issue.id))


  ################ ###########################
 
@login_required
def get_detail(request, issue_id):

    """
    Create a view that allow Authenticated user 
    to see the details and comments of the issue.
     
    """
    detailissue = get_object_or_404(Issue, pk=issue_id)
    comments = Comment.objects.all()
    return render(request, 'issue/detail.html', {'issue': detailissue})

 ############# Comment #######################

@login_required       
def create_comment(request, pk):

    """
    Create a view that allow Authenticated user 
    to comment on the issue.
     
    """
    comments = Comment.objects.all()
    issue = get_object_or_404(Issue, pk=pk) if pk else None
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.created_by = request.user
            form.instance.issue = issue
            form.save()
            return redirect('/issue/' +str(issue.id))
    else:
        form = CommentForm()
    return render(request, 'issue/commentform.html', {'form': form, 'comments': comments})


        
@login_required   
def edit_comment(request, pk):

    """
    Create a view that allow Authenticated user 
    to edit own comment on the issue.
     
    """
    comment = get_object_or_404(Comment, pk=pk)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('/issue/' + str(comment.issue.pk))
    else:
        form = CommentForm(instance=comment)
    return render(request, 'issue/commentform.html', {'form': form})

#########################################################################################

