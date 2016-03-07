from django.test import TestCase
from .models import Entry


class BlogPostTest(TestCase):

    def test_create_unpublished(self):
        entry = Entry(title="Title Me", body=" ", publish=False)
        entry.save()
        self.assertEqual(Entry.objects.all().count(), 1)
        self.assertEqual(Entry.objects.published().count(), 0)
        entry.publish = True
        entry.save()
        self.assertEqual(Entry.objects.published().count(), 1)


class BlogViewTests(TestCase):
    def test_feed_url(self):
        response = self.client.get('/feed/')
        self.assertIn("xml", response['Content-Type'])