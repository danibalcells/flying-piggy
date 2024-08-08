from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SavingsEntry, SavingsGoal
from .forms import SavingsEntryForm, SavingsGoalForm

@login_required
def add_entry(request):
    if request.method == 'POST':
        form = SavingsEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('home')
    else:
        form = SavingsEntryForm()
    return render(request, 'add_entry.html', {'form': form})

@login_required
def add_goal(request):
    if request.method == 'POST':
        form = SavingsGoalForm(request.POST)
        if form.is_valid():
            goal = form.save()
            goal.users.add(request.user)
            return redirect('home')
    else:
        form = SavingsGoalForm()
    return render(request, 'add_goal.html', {'form': form})

@login_required
def home(request):
    goals = SavingsGoal.objects.filter(users=request.user)
    goal_progress = []

    for goal in goals:
        total_saved = SavingsEntry.objects.filter(user=request.user, goal=goal).aggregate(total=Sum('amount'))['total'] or 0
        progress_percentage = (total_saved / goal.target_amount) * 100 if goal.target_amount > 0 else 0
        goal_progress.append({
            'goal': goal,
            'total_saved': total_saved,
            'progress_percentage': progress_percentage
        })

    latest_entries = SavingsEntry.objects.filter(user=request.user).order_by('-date')[:5]

    return render(request, 'home.html', {'goal_progress': goal_progress, 'latest_entries': latest_entries})