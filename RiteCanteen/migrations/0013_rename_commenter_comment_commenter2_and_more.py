# Generated by Django 4.1.7 on 2023-03-12 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RiteCanteen', '0012_remove_comment_rite_comment_love'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Commenter',
            new_name='Commenter2',
        ),
        migrations.AlterField(
            model_name='comment',
            name='love',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments2', to='RiteCanteen.continental2'),
        ),
    ]
