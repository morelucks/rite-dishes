# Generated by Django 4.1.7 on 2023-03-12 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RiteCanteen', '0009_remove_comment_love_comment_rite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rite',
        ),
        migrations.AddField(
            model_name='comment',
            name='love',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='RiteCanteen.continental2'),
        ),
    ]
