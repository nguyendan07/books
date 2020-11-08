from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTest(TestCase):
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
