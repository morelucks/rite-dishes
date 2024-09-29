# Generated by Django 4.1.7 on 2023-04-02 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiteWeb', '0025_remove_userprofileinfo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Customer', 'Customer')], default='Customer', max_length=10),
        ),
    ]
