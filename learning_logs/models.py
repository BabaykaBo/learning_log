from django.db import models
from  django.contrib.auth.models import User


# Create your models here.

class Topic(models.Model):
    """Тема, яку вивчає користувач"""
    objects = None
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Повернути рядкове представлення моделі"""
        return self.text


class Entry(models.Model):
    """Інформація до теми"""
    objects = None
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."
