# Generated by Django 4.1.7 on 2023-04-01 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiteWeb', '0023_ritegallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
