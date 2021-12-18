from django.db import models

class User(models.Model):
    account = models.CharField(max_length=20)
    name = models.CharField(max_length=20, null = True)
    email = models.EmailField(max_length=100, null = True)

    def __str__(self):
        return self.name

class Msg(models.Model):
    score = models.IntegerField(null = True)
    memo = models.CharField(max_length=200, null = True)
    user_id = models.ForeignKey(
        "User", on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.name + "-" + str(self.score)
