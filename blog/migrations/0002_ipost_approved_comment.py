# Generated by Django 2.0.13 on 2019-10-01 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipost',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]
