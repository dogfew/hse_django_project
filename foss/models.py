
from django.db import models


class Person(models.Model):
    # foss_person
    first_name = models.CharField(max_length=100, )
    second_name = models.CharField(max_length=100, )
    phone = models.CharField(max_length=20, )
    email = models.CharField(max_length=50)
    date = models.DateTimeField('date published', auto_now_add=True)


class Opinion(models.Model):
    # foss_opinion
    distro_name = models.CharField(max_length=100)
    rate = models.IntegerField()
    opinion = models.CharField(max_length=500)
    date = models.DateTimeField('date published', auto_now_add=True)


class Task(models.Model):
    # foss_task
    expected_value = models.IntegerField()
    answer = models.IntegerField()
    prime_num = models.IntegerField()