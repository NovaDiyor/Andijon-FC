# Generated by Django 4.1 on 2022-11-17 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_game_helps_remove_game_kross_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='passes',
            name='percent',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='passes',
            name='status',
            field=models.IntegerField(choices=[(1, 'passes'), (2, 'long-passes'), (3, 'helps'), (4, 'crosses')]),
        ),
        migrations.AlterField(
            model_name='players',
            name='position',
            field=models.IntegerField(choices=[(1, 'forward'), (4, 'goalkeeper'), (3, 'defender'), (2, 'midfielder')], default=1),
        ),
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.IntegerField(choices=[(6, 'admin'), (1, 'trainer'), (3, 'physiotherapist'), (2, 'sub-trainer'), (5, 'goalkeeper-trainer'), (4, 'doctor')]),
        ),
    ]