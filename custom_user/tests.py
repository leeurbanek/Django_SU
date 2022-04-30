from django.contrib.auth import get_user_model
from django.test import TestCase


# Create your tests here.

class CustomUserTests(TestCase):
    """"""
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='user1',
            email='user1@email.com',
            password='pass1'
        )
        self.assertEqual(user.username, 'user1')
        self.assertEqual(user.email, 'user1@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        suser = User.objects.create_superuser(
            username='suser1',
            email='suser1@email.com',
            password='spass1'
        )
        self.assertEqual(suser.username, 'suser1')
        self.assertEqual(suser.email, 'suser1@email.com')
        self.assertTrue(suser.is_active)
        self.assertTrue(suser.is_staff)
        self.assertTrue(suser.is_superuser)


# class MessagePageTests(TestCase):
#     """"""
#     username = 'user1'
#     email = 'user1@email.com'

#     def setUp(self):
#         url = reverse('message')
#         self.response = self.client.get(url)
