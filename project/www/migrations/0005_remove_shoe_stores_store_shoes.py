# Generated by Django 4.1 on 2024-05-25 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0004_shoe_stores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='stores',
        ),
        migrations.AddField(
            model_name='store',
            name='shoes',
            field=models.ManyToManyField(to='www.shoe'),
        ),
    ]
