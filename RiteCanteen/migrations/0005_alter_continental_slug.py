# Generated by Django 4.1.7 on 2023-03-10 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiteCanteen', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='continental',
            name='slug',
            field=models.SlugField(),
        ),
    ]
