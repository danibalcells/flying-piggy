from decimal import Decimal
from django.utils import timezone
from django.contrib.auth.models import User
from .models import SavingsGoal, SavingsEntry, UserProfile

class UserContribution:
    def __init__(self, user):
        self.user = user
        self.amount = Decimal('0.00')
        self.profile = UserProfile.objects.get(user=user)

    @property
    def color(self):
        return self.profile.progress_color

    @property
    def image(self):
        return self.profile.profile_image

class GoalProgress:
    def __init__(self, goal):
        self.goal = goal
        self.total_saved = Decimal('0.00')
        self.user_contributions = {user.username: UserContribution(user) for user in User.objects.all()}

    @property
    def progress_percentage(self):
        return (self.total_saved / self.goal.target_amount) * 100

    @property
    def days_left(self):
        return (self.goal.date - timezone.now().date()).days

    def add_contribution(self, entry):
        amount_to_add = min(entry.amount, self.goal.target_amount - self.total_saved)
        self.total_saved += amount_to_add
        self.user_contributions[entry.user.username].amount += amount_to_add
        return amount_to_add

def calculate_progress():
    goals = SavingsGoal.objects.all().order_by('date')
    entries = SavingsEntry.objects.all().order_by('date')
    
    progress = []
    remaining_savings = Decimal('0.00')
    
    for goal in goals:
        goal_progress = GoalProgress(goal)
        
        # Add any remaining savings from previous goals
        goal_progress.total_saved += remaining_savings
        
        # Calculate savings for this goal
        for entry in entries.filter(date__lte=goal.date):
            if goal_progress.total_saved < goal.target_amount:
                amount_added = goal_progress.add_contribution(entry)
                entry.amount -= amount_added
                if entry.amount == 0:
                    entries = entries.exclude(id=entry.id)
            else:
                break
        
        # Calculate remaining savings for next goal
        if goal_progress.total_saved > goal.target_amount:
            remaining_savings = goal_progress.total_saved - goal.target_amount
            goal_progress.total_saved = goal.target_amount
        else:
            remaining_savings = Decimal('0.00')
        
        progress.append(goal_progress)
    
    return progress