from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.

class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        return Post.objects.create(
            author = User.objects.get(id=1),
            title = 'ieieieiei',
            body = 'akioerieuieowr',
        )