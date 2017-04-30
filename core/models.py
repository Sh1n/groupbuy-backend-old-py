from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')


class Offer(models.Model):
    '''
        Subject of purchase
    '''
    user = models.ForeignKey('auth.User', related_name='offers', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    goal_qnt = models.IntegerField()
    deadline = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    discount_perc = models.DecimalField(max_digits=10,decimal_places=2)
    expedition_price = models.DecimalField(max_digits=10,decimal_places=2)

    participants = models.ManyToManyField(User)


class Notification(models.Model):
    '''
        Notification to be read from for the user
    '''
    user = models.ForeignKey('auth.User', related_name='notifications', on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('pub_date','read')
