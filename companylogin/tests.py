from django.test import TestCase

# simple smoke tests for question management
from django.urls import reverse
from .models import Question


class QuestionTests(TestCase):
	def setUp(self):
		# create a dummy question
		Question.objects.create(
			question="What is 2+2?",
			option_1="1",
			option_2="2",
			option_3="3",
			option_4="4",
			correct_option="4",
			marks=1,
			topic="Math",
			difficulty="Easy",
			generated_by="manual",
		)

	def test_question_str(self):
		q = Question.objects.first()
		self.assertIn("Math", str(q))

	def test_questions_view_requires_login(self):
		# without session should redirect to homepage
		resp = self.client.get(reverse('questions'))
		self.assertEqual(resp.status_code, 302)

	def test_delete_question(self):
		# call the view directly with a session-enabled request so the
		# deletion logic runs deterministically (avoids client cookie issues)
		from django.test.client import RequestFactory
		from django.contrib.sessions.middleware import SessionMiddleware
		from companylogin.views import delete_question

		q = Question.objects.first()
		rf = RequestFactory()
		req = rf.get(reverse('delete_question', args=[q.id]))
		# attach a session to the request
		middleware = SessionMiddleware(lambda r: None)
		middleware.process_request(req)
		req.session['com_id'] = 1
		req.session.save()
		resp = delete_question(req, q.id)
		self.assertEqual(getattr(resp, 'status_code', None), 302)
		self.assertFalse(Question.objects.filter(id=q.id).exists())

# Create your tests here.
