from django.db import models
from django.contrib.auth.models import User

class SavingsGoal(models.Model):
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class SavingsEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    goal = models.ForeignKey(SavingsGoal, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.amount} - {self.description[:20]}"

class Shortcut(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    emoji = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.emoji} {self.name}"