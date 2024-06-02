from django.db import models
from .models import Post

class PostCreate:
    @staticmethod
    def save(title, text):
        post = Post(title=title, text=text)
        post.save()
        return post