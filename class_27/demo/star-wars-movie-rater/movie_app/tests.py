from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from movie_app.models import Movie

# Create your tests here.

class MoviesTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.movie = Movie.objects.create(
            name = 'Empire', rating = 10, reviewer = self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.movie), 'Empire')

    def test_movie_name(self):
        self.assertEqual(f'{self.movie.name}', 'Empire')

    def test_list_page_status_code(self):
        url = reverse("movie_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("movie_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "movie_list.html")
        self.assertTemplateUsed(response, "base.html")
