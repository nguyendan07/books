from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignupPageView


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='dannv',
            email='dannv@email.com',
            password='testpass123456'
        )
        self.assertEqual(user.username, 'dannv')
        self.assertEqual(user.email, 'dannv@email.com')
        self.assertTrue(user.is_active),
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superadmin',
            email='admin@superuser.com',
            password='123456a@'
        )
        self.assertEqual(user.username, 'superadmin')
        self.assertEqual(user.email, 'admin@superuser.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.resp = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.resp.status_code, 200)
        self.assertTemplateUsed(self.resp, 'signup.html')
        self.assertContains(self.resp, 'Sign Up')
        self.assertNotContains(self.resp, 'Hi there! I should not be on the page.')
    
    def test_signup_form(self):
        form = self.resp.context.get('form')
        # self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
    
    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
