# Generated by Django 4.2.4 on 2023-08-27 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogwebsite',
            name='category',
            field=models.CharField(choices=[('FASHION', 'Fashion'), ('BEAUTY', 'Beauty'), ('TRAVEL', 'Travel'), ('PERSONAL', 'Personal'), ('TECH', 'Tech'), ('HEALTH', 'Health'), ('HOME', 'Home'), ('FITNESS', 'Fitness'), ('EDUCATION', 'Education'), ('FOOD', 'Food'), ('ENTERTAINMENT', 'Entertainment')], default='blog', max_length=512),
        ),
    ]
