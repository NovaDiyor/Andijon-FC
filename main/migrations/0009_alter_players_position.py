# Generated by Django 4.1 on 2022-11-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_players_sub_captain_alter_players_captain_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='position',
            field=models.IntegerField(choices=[(3, 'defender'), (2, 'midfielder'), (4, 'goalkeeper'), (1, 'forward')], default=1),
        ),
    ]