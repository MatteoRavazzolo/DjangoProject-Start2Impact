from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def clean(self):
        prohibited_words = ['hack']
        for object in self.content.split():
            if object in prohibited_words:
                raise ValidationError('You\'re trying to write a post with prohibited words')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Post, self).save(*args, **kwargs)
 
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



    





