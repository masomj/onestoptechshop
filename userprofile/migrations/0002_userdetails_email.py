# Generated by Django 4.0.6 on 2023-01-07 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='email',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
