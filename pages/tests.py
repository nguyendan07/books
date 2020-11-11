from django.test import SimpleTestCase
from django.urls import reverse


# class HomePageTest(SimpleTestCase):
#     def test_homepage_status_code(self):
#         resp = self.client.get('/')
#         self.assertEqual(resp.status_code, 200)
    
#     def test_homepage_url_name(self):
#         resp = self.client.get(reverse('home'))
#         self.assertEqual(resp.status_code, 200)
    
#     def test_homepage_template(self):
#         resp = self.client.get('/')
#         self.assertTemplateUsed(resp, 'home.html')
#         self.assertContains(resp, 'Homepage')
#         self.assertNotContains(resp, 'Hi there! I should not be on the page.')
class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
