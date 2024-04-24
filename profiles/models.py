from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    CUSTOMER = 'CU'
    PERFORMER = 'PE'
    USER_TYPE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (PERFORMER, 'Performer'),
    ]
    user_type = models.CharField(
        max_length=2, choices=USER_TYPE_CHOICES, default=CUSTOMER)

    def is_customer(self):
        return self.user_type == self.CUSTOMER

    def is_performer(self):
        return self.user_type == self.PERFORMER

    def __str__(self):
        return f'<Пользователь: {self.username}>'


User = CustomUser()


class CustomerProfile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=100)
    experience = models.TextField()

    def __str__(self):
        return f'<Покупатель: {self.name}>'


class PerformerProfile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=100)
    experience = models.TextField()

    def __str__(self):
        return f'<Исполнитель: {self.name}>'
