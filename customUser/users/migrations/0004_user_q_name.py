# Generated by Django 2.2.6 on 2019-10-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191017_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='q_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
