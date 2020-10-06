from django.test import TestCase
from faker import Faker

from users.models import User


class UserTest(TestCase):
    def test_follow(self):
        faker = Faker()

        user_a = User.objects.create_user(username=faker.profile().get("username"), password=faker.password())
        user_b = User.objects.create_user(username=faker.profile().get("username"), password=faker.password())
        user_a.follow(user_b)

        user_a.refresh_from_db()
        user_b.refresh_from_db()

        self.assertEqual(user_a.followed.count(), 1)
        self.assertEqual(user_a.followers.count(), 0)
        self.assertEqual(user_b.followers.count(), 1)
        self.assertEqual(user_b.followed.count(), 0)
