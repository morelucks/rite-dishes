# Generated by Django 4.1.7 on 2023-04-04 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiteWeb', '0027_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='body2',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='body3',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='body4',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='body',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]