# Generated by Django 5.1.1 on 2024-09-07 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Emoloyee',
            new_name='Employee',
        ),
    ]