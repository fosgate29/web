# Generated by Django 2.2.4 on 2020-04-12 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('townsquare', '0017_squelchprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_edited',
            field=models.BooleanField(default=False),
        ),
    ]