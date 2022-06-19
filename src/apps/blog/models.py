from django.db import models
from django.shortcuts import reverse


class Article(models.Model):
    title = models.CharField(max_length=128)
    banner = models.ImageField(upload_to='articles', blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True, blank=True)
    published = models.BooleanField(default=True, blank=True)

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
