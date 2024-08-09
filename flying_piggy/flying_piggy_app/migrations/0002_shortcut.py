# Generated by Django 5.1 on 2024-08-08 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flying_piggy_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shortcut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=255)),
                ('emoji', models.CharField(max_length=10)),
            ],
        ),
    ]
