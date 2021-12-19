from django.db import models
from django.urls import reverse 

class User(models.Model):
    account = models.CharField(max_length=20)
    name = models.CharField(max_length=20, null = True)
    email = models.EmailField(max_length=100, null = True)

    class Meta:
        ordering = ['-account', '-name']

    def __str__(self):
        return self.name

class Msg(models.Model):
    user_id = models.ForeignKey(
        "User", on_delete=models.CASCADE)
    score = models.IntegerField(null = True)
    memo = models.CharField(max_length=200, null = True)
    date = models.DateTimeField()

    def get_url(self):
        return reverse('msg-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-date', '-user_id']

    def __str__(self):
        return self.user_id.name + "-" + str(self.score)
