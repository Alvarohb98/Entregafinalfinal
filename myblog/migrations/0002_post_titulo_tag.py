# Generated by Django 4.2 on 2023-04-05 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='titulo_tag',
            field=models.CharField(default='Travel Blog!', max_length=30),
        ),
    ]