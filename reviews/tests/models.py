from django.test import TestCase

from reviews.models import Review
from django.contrib.auth.models import User 

class TestReviews(TestCase):

    @classmethod
    def setUpTestData(cls):
        print('custom setup ')
        cls.count = Review.objects.count()
        cls.a = User.objects.create(username='quantum', password='testing')
        cls.b = User.objects.create(username='poloko', password='yoyo')
        cls.r = Review.objects.create(email='ikeecode@gmail.com', comment='Oya captain, You dey play with T-Play ', rating=3)
        cls.r.likes.set([cls.a.pk, cls.b.pk])

    def test_review_model_exist(self): 
        self.assertTrue(self.count==0)

    # you might not need to test this thooooooooooooooooooooooooooooooooooo
    def test_users_like_review(self):
        self.assertEqual(self.r.likes.count(), 2)


