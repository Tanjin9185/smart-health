# Generated by Django 3.1.3 on 2021-01-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0045_auto_20210114_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verified',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=10, null=True),
        ),
    ]