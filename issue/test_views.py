from django.test import TestCase
from django.contrib.auth.models import User
from .models import Issue, Comment
from django.urls import reverse

class LoggedInTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='Customer1', password='Pass1234')
        self.client.login(username='Customer1', password='Pass1234')


class TestViews(LoggedInTestCase):


    def test_get_edit_issue_page(self):
        user = User()
        user.save()
        issue = Issue(name="Test Issue Name", description="Test Issue Description", created_by=user, price=100)
        issue.save()
        page = self.client.get("/issue/edit/{0}?/".format(issue.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issue/issueform.html")

    def test_get_issue_detail_page(self):
        user = User()
        user.save()
        issue = Issue(name="Test Issue Name", description="Test Issue Description", created_by=user, price=100)
        issue.save()
        page = self.client.get("/issue/{0}/".format(issue.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issue/detail.html")

    def test_get_edit_issue_page_for_item_that_does_not_exist(self):
        page = self.client.get("/issues/1/edit/")
        self.assertEqual(page.status_code, 404)

    def test_get_issue_detail_page_for_item_that_does_not_exist(self):
        page = self.client.get("/issues/1/")
        self.assertEqual(page.status_code, 404)


    def test_get_add_comment_page(self):
        user = User()
        user.save()
        issue = Issue(name="Test Issue Name", description="Test Issue Description", created_by=user, price=100)
        issue.save()
        page = self.client.get("/issue/{0}/new/".format(issue.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issue/commentform.html")

    def test_get_edit_comment_page(self):
        user = User()
        user.save()
        issue = Issue(name="Test Issue Name", description="Test Issue Description", created_by=user, price=100)
        issue.save()
        comment = Comment(comment="Test Issue Comment", created_by=user, issue=issue)
        comment.save()
        page = self.client.get("/issue/{0}/edit/".format(issue.id, comment.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issue/commentform.html")


    def test_get_edit_comment_page_for_item_that_does_not_exist(self):
        page = self.client.get("/issues/1/1/edit/")
        self.assertEqual(page.status_code, 404)

