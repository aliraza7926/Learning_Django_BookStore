from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve


class CustomUserTests(TestCase):
    
    def test_create_user(self):
        User=get_user_model()
        user=User.objects.create_user(
            username="ali",
            email="ali@mail.com",
            password="a"
        )

        self.assertEqual(user.username, "ali")
        self.assertEqual(user.email, "ali@mail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        
        User=get_user_model()
        admin_user=User.objects.create_superuser(
            username="admin",
            email="admin@mail.com",
            password="password"
        )

        self.assertEqual(admin_user.username, "admin")
        self.assertEqual(admin_user.email, "admin@mail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)



