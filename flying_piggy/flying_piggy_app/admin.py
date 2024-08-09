from django.contrib import admin
from .models import SavingsGoal, SavingsEntry, Shortcut

# Register your models here.
admin.site.register(SavingsGoal)
admin.site.register(SavingsEntry)
admin.site.register(Shortcut)