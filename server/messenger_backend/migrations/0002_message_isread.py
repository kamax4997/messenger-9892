# Generated by Django 3.2.4 on 2021-10-04 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='isRead',
            field=models.BooleanField(default=False),
        ),
    ]