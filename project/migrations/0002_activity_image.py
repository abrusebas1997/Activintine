# Generated by Django 2.2.7 on 2020-03-19 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='activity_pic'),
        ),
    ]
