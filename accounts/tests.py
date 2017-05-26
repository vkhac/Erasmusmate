# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from accounts.models import Profile, UserProfile
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your tests here.


class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user2 = User.objects.create(username="testuser")
        self.userprofile = UserProfile.objects.create(
            user=self.user2,
            sex="male",
            university="AGH",
            country_of_origin="Greece",
            faculty="informatyka",
            user_id = 101,
            age=18,
            email = "user@email.com",
            prefered_cuisine = "CHINESE"
        )

        self.date = timezone.now()


    def test_default_values(self):
        self.assertEqual(self.user2, self.userprofile.user)
        self.assertEqual(self.userprofile.sex, "male")
        self.assertEqual(self.userprofile.country_of_origin, "Greece")
        self.assertEqual(self.userprofile.faculty, "informatyka")
        self.assertEqual(self.userprofile.age, 18)
        self.assertEqual(self.userprofile.university, "AGH")
        self.assertEqual(self.userprofile.email, "user@email.com")
        self.assertEqual(self.userprofile.phone, 0)
        self.assertEqual(self.userprofile.country_of_studies, "")
        self.assertEqual(self.userprofile.city_of_studies, "")
        self.assertEqual(self.userprofile.region, "")
        self.assertIn(self.userprofile.prefered_cuisine, dict(UserProfile.CUISINE_CHOICES))
        self.assertEqual(self.userprofile.description, "")
        self.assertIsNone(self.userprofile.image._file)
        self.assertIn(self.userprofile.hardworking, dict(UserProfile.RATE_CHOICES))
        self.assertIn(self.userprofile.partying, dict(UserProfile.RATE_CHOICES))
        self.assertIn(self.userprofile.traveling, dict(UserProfile.RATE_CHOICES))
        self.assertEqual(self.userprofile.price, 0)
        self.assertIn(self.userprofile.smoking_permitted, dict(UserProfile.RATE_CHOICES))
        self.assertIn(self.userprofile.same_nationality_roommates, dict(UserProfile.CHOICES))
        self.assertIn(self.userprofile.time_of_staying_in_flat, dict(UserProfile.TIME_CHOICES))
        self.assertIn(self.userprofile.men_or_women_on_room, dict(UserProfile.MEN_OR_WOMEN_CHOICES))
        self.assertIn(self.userprofile.num_of_roommates, dict(UserProfile.NUM_OF_PEOPLE_CHOICES))
        self.assertTrue(abs(self.userprofile.date-self.date)<timezone.timedelta(seconds=1))


    def test_str(self):
        self.assertEqual(self.userprofile.__str__(), "Profile of testuser")


class UserTestCase(TestCase):
    def get_page(self, url):
        """ Ensures given url returns HTTP 200. """
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        return response

    def page_redirect(self, url):
        """ Ensure given url returns HTTP 302 """
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        return response

    def page_404(self, url):
        """ Ensure given url returns HTTP 404 """
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        return response

    def login(self):
        login = self.client.login(username='admin', password='admin')
        self.assertEqual(login, True)

    def logout(self):
        self.client.logout()

    def test_view_profile(self):
        self.get_page(reverse('accounts:view_profile'))
