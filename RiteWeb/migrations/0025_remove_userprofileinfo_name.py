# Generated by Django 4.1.7 on 2023-04-01 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RiteWeb', '0024_userprofileinfo_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='name',
        ),
    ]
