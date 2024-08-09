from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class SavingsGoal(models.Model):
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    image = models.ImageField(upload_to='goal_images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Savings goal"
        verbose_name_plural = "Savings goals"

class SavingsEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.amount} - {self.description[:20]}"

    class Meta:
        verbose_name = "Savings entry"
        verbose_name_plural = "Savings entries"

class Shortcut(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    emoji = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.emoji} {self.name}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    progress_color = models.CharField(max_length=7, default='#000000')  # Hex color code

    def __str__(self):
        return self.user.username