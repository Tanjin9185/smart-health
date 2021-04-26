# Generated by Django 3.1.4 on 2021-03-11 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0052_auto_20210311_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='days',
        ),
        migrations.AddField(
            model_name='schedule',
            name='days',
            field=models.ManyToManyField(null=True, related_name='days', to='users.Days', verbose_name='Select Days'),
        ),
    ]
