# Generated by Django 3.2.5 on 2021-08-06 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Entities', '0012_auto_20210806_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='client',
            name='password',
        ),
    ]