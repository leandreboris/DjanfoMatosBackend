# Generated by Django 3.2.5 on 2021-08-05 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Entities', '0010_alter_article_imagearticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='facture',
            name='clientFacture',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Entities.client'),
            preserve_default=False,
        ),
    ]
