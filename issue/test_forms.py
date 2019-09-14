from django.test import TestCase
from .forms import IssueForm, CommentForm


# Create your tests here.
class TestDjango(TestCase):

    def test_issue_form_can_submit_with_required_fields(self):
        form = IssueForm({'name': 'Test Name', 'description': 'Test Description', 'varieties': 'Bug'})
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_issue_form_correct_error_message_for_missing_required_fields(self):
        form = IssueForm({'name': ''}, {'description': ''}, {'varieties': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
        self.assertEqual(form.errors['description'], [u'This field is required.'])
        self.assertEqual(form.errors['varieties'], [u'This field is required.'])

    def test_comment_form_can_submit_with_required_field(self):
        form = CommentForm({'comment': 'Test Comment'})
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_comment_form_correct_error_message_for_missing_required_field(self):
        form = CommentForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['comment'], [u'This field is required.'])
