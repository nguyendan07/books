from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTest(SimpleTestCase):
    def test_homepage_status_code(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_homepage_url_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_homepage_template(self):
        resp = self.client.get('/')
        self.assertTemplateUsed(resp, 'home.html')
        self.assertContains(resp, 'Homepage')
        self.assertNotContains(resp, 'Hi there! I should not be on the page.')        
