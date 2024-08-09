from django.utils import timezone
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SavingsEntry, SavingsGoal, Shortcut
from .forms import SavingsEntryForm, SavingsGoalForm, ShortcutForm
from .progress import calculate_progress

@login_required
def add_entry(request):
    if request.method == 'POST':
        form = SavingsEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('progress')
    else:
        form = SavingsEntryForm()
    shortcuts = Shortcut.objects.all()
    return render(request, 'add_entry.html', {'form': form, 'shortcuts': shortcuts})

@login_required
def add_goal(request):
    if request.method == 'POST':
        form = SavingsGoalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('progress')
    else:
        form = SavingsGoalForm()
    return render(request, 'add_goal.html', {'form': form})

@login_required
def progress(request):
    goal_progress = calculate_progress()
    current_date = timezone.now().date()
    current_goal_index = next((i for i, progress in enumerate(goal_progress) if progress.goal.date > current_date), 0)
    return render(request, 'progress.html', {
        'goal_progress': goal_progress,
        'current_goal_index': current_goal_index
    })

@login_required
def add_shortcut(request):
    if request.method == 'POST':
        form = ShortcutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('progress')
    else:
        form = ShortcutForm()
    return render(request, 'add_shortcut.html', {'form': form})