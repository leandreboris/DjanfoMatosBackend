# Generated by Django 3.2.5 on 2021-08-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entities', '0008_auto_20210803_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='imageArticle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
