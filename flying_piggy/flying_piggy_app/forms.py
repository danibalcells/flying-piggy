from django import forms
from .models import SavingsEntry, SavingsGoal, Shortcut

class SavingsEntryForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(attrs={'size': '40'}),
        required=False
    )

    class Meta:
        model = SavingsEntry
        fields = ['amount', 'description']

class SavingsGoalForm(forms.ModelForm):
    class Meta:
        model = SavingsGoal
        fields = ['name', 'target_amount', 'date', 'image']

class ShortcutForm(forms.ModelForm):
    class Meta:
        model = Shortcut
        fields = ['name', 'amount', 'description', 'emoji']