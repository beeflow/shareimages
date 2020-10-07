from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APIClient


class AuthTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.faker = Faker()

    def test_register(self):
        profile, password = self.faker.profile(), self.faker.password()
        response = self.client.post(
            reverse("api:register"),
            {"username": profile.get("username"), "password": password, "email": profile.get("email")},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            get_user_model().objects.get(username=profile.get("username")).username, profile.get("username")
        )

    def test_login(self):
        username, password = self.faker.first_name(), self.faker.password()
        get_user_model().objects.create_user(username=username, password=password)

        response = self.client.post(reverse("api:login"), {"username": username, "password": password}, format="json")
        self.assertIsNotNone(response.data.get("auth_token"))


class UsersListTest(TestCase):
    def setUp(self) -> None:
        self.faker = Faker()
        self.client = APIClient()
        self.UserModel = get_user_model()

    def test_users_list_only_for_logged(self):
        username, password = self.faker.first_name(), self.faker.password()

        self.UserModel.objects.create_user(username=username, password=password)
        self.UserModel.objects.create_user(
            username=self.faker.profile().get("username"), password=self.faker.password()
        )

        response = self.client.get(reverse("api:users"), format="json")
        self.assertEqual(response.data.get("detail"), "Authentication credentials were not provided.")

    def test_users_list(self):
        username, password = self.faker.first_name(), self.faker.password()

        self.UserModel.objects.create_user(username=username, password=password)
        self.UserModel.objects.create_user(
            username=self.faker.profile().get("username"), password=self.faker.password()
        )

        response = self.client.post(reverse("api:login"), {"username": username, "password": password}, format="json")
        token = response.data.get("auth_token")

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        response = self.client.get(reverse("api:users"), format="json")

        self.assertEqual(response.data.get("count"), 2)
