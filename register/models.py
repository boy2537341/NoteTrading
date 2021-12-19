from django.db import models
# Create your models here.

class User(models.Model):
    SUGGEST_CHOICES = [
        ('1', '非常不滿意'),
        ('2', '不滿意'),
        ('3', '普通'),
        ('4', '滿意'),
        ('5', '非常滿意')
    ]

    account = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    score = models.IntegerField(blank=False)
    memo = models.TextField(max_length=200, blank=False)
    suggest_id = models.CharField(max_length=1, choices = SUGGEST_CHOICES, default='5')

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name
