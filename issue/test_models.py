from django.test import TestCase
from .models import Issue, Comment
from django.contrib.auth.models import User


class TestIssueModel(TestCase):


    def test_create_issue(self):
        user = User()
        user.save()
        issue = Issue(name="Test Issue Name", description="Test Issue Description", created_by=user, price=100)
        issue.save()
        self.assertEqual(issue.name, "Test Issue Name")
        self.assertEqual(issue.description, "Test Issue Description")
        self.assertEqual(issue.created_by, user)
        self.assertEqual(issue.price, 100)
        self.assertEqual(issue.varieties, "Bug")
        self.assertEqual(issue.status, "To do")
        self.assertEqual(issue.upvotes, 1)
       

    def test_create_comment(self):
        user = User()
        user.save()
        issue = Issue(name="Test Issue Name", description="Test Issue Description", created_by=user, price=100)
        issue.save()
        comment = Comment(comment="Test Issue Comment", created_by=user, issue=issue)
        comment.save()
        self.assertEqual(comment.comment, "Test Issue Comment")
        self.assertEqual(comment.created_by, user)
        self.assertEqual(comment.issue, issue)


