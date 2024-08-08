from django import forms
from .models import SavingsEntry, SavingsGoal

class SavingsEntryForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(attrs={'size': '40'}),
        required=False
    )

    class Meta:
        model = SavingsEntry
        fields = ['amount', 'description', 'goal']

class SavingsGoalForm(forms.ModelForm):
    class Meta:
        model = SavingsGoal
        fields = ['name', 'target_amount']