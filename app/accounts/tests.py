from django.test import TestCase


class Sanity(TestCase):
    def test_a(self):
        self.assertIs(True, True)
