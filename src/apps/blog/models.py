from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=128)
    banner = models.ImageField(upload_to='articles', blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True, blank=True)
    published = models.BooleanField(default=True, blank=True)

