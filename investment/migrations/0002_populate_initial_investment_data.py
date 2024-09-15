# Generated by Django 5.1.1 on 2024-09-15 19:35

from django.db import migrations

from investment.utils import create_update_investment_accounts


class Migration(migrations.Migration):
    dependencies = [
        ('investment', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_update_investment_accounts),
    ]
