# Generated by Django 4.1 on 2022-11-15 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_guestaction_which_remove_substitute_seconds_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='position',
            field=models.IntegerField(choices=[(2, 'midfielder'), (1, 'forward'), (3, 'defender'), (4, 'goalkeeper')], default=1),
        ),
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.IntegerField(choices=[(2, 'sub-trainer'), (1, 'trainer'), (5, 'goalkeeper-trainer'), (6, 'admin'), (3, 'physiotherapist'), (4, 'doctor')]),
        ),
    ]
