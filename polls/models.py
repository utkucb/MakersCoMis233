from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    message = models.CharField(max_length=200)


class Choise(models.Model):
    name = models.CharField(max_length=200)
    palet_choise = models.IntegerField()
    photo_choise = models.IntegerField()

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

# Create your models here.
