from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=200, unique=True)
    opis = models.TextField(default='Opis')
    choroby = models.TextField(default='Choroby')
    zastosowanie = models.TextField(default='Zastosowanie')
    zdjecie = models.ImageField(default='default.png')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nazwa

class Post_apteczka(models.Model):
    ziola = models.ManyToManyField(Post)
