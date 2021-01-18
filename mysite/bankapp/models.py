from django.contrib.auth.models import User
from django.db import models

TYPE_CHOICES = (
    ("Debit", "Debit"),
    ("Credit", "Credit"),
)


class Bank(models.Model):
    contact_number = models.CharField(max_length=11)
    name = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    number = models.CharField(max_length=11)
    title = models.CharField(max_length=200)
    balance = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


# class Transaction(models.Model):
#     transaction_t = models.ForeignKey(Bank, on_delete=models.CASCADE)
#     transaction_f = models.ForeignKey(Bank, on_delete=models.CASCADE)
#     amount = models.FloatField()
#     type = models.CharField(choices=TYPE_CHOICES, max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()


