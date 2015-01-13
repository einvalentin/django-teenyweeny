from django.test import TestCase
from .models import ShortLink
from django.core.urlresolvers import reverse

class RedirectionTests(TestCase):
    def setUp(self):
        self.short = 'test'
        self.url = 'https://www.google.de/#safe=off&q=best+url+shortener'
        self.link = ShortLink(short=self.short, link=self.url)
        self.link.save()

    def test_redirection(self):
        resp = self.client.get(reverse('redirect', kwargs={'short_link': 'test'}))
        self.assertEquals(301, resp.status_code)
        self.assertEquals(self.url, resp['Location'])

    def test_invalid_link(self):
        resp = self.client.get(reverse('redirect', kwargs={'short_link': 'not_available'}))
        self.assertEquals(404, resp.status_code)

    def test_link_counter_increment(self):
        old = self.link.hit
        self.client.get(reverse('redirect', kwargs={'short_link': 'test'}))
        self.assertEquals(old+1, ShortLink.objects.get(short=self.short).hit)

