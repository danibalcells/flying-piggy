# Generated by Django 5.1 on 2024-08-09 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flying_piggy_app', '0003_remove_savingsentry_goal_savingsgoal_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='savingsentry',
            options={'verbose_name_plural': 'Savings entries'},
        ),
        migrations.RemoveField(
            model_name='savingsgoal',
            name='users',
        ),
    ]
