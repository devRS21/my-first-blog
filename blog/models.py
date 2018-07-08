from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length = 500)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    picture = models.ImageField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
