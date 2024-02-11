from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class Test(TestCase):
    def test_casoVS(self):
        url = "/"

        request = self.client.get(url)

        self.assertEqual(request.status_code, 200)
