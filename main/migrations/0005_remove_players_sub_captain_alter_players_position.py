# Generated by Django 4.1 on 2022-11-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_players_sub_captain_alter_players_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='sub_captain',
        ),
        migrations.AlterField(
            model_name='players',
            name='position',
            field=models.IntegerField(choices=[(4, 'goalkeeper'), (2, 'midfielder'), (3, 'defender'), (1, 'forward')], default=1),
        ),
    ]
