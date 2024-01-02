from django.db import models
from django.urls import reverse


class Tag(models.Model):
    tags = models.CharField(max_length=50)

    def __str__(self):
        return self.tags


class Post(models.Model):
    author_post = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description_post = models.TextField()
    quantity_likes = models.PositiveIntegerField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.author_post} - {self.title}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
