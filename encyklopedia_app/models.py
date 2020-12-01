from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
    published_date = models.DateTimeField(default=timezone.now,
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nazwa

class ListaZiol(models.Model):
    ziola = models.ManyToManyField(Post)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.DO_NOTHING)

    @classmethod
    def dodaj_ziolo(cls, current_user, nowe_ziolo):
        listaziol, created = cls.objects.get_or_create(
            current_user = current_user
        )
        listaziol.ziola.add(nowe_ziolo)

    @classmethod
    def usun_ziolo(cls, current_user, nowe_ziolo):
        listaziol, created = cls.objects.get_or_create(
            current_user = current_user
        )
        listaziol.ziola.remove(nowe_ziolo)
