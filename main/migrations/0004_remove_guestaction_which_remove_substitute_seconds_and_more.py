# Generated by Django 4.1 on 2022-11-15 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_host_goal_game_host_action_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestaction',
            name='which',
        ),
        migrations.RemoveField(
            model_name='substitute',
            name='seconds',
        ),
        migrations.AddField(
            model_name='action',
            name='club_who',
            field=models.CharField(default=1, max_length=210),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fc',
            name='status',
            field=models.IntegerField(choices=[(1, 'Fc'), (2, 'Club')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fc',
            name='trainer',
            field=models.CharField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='fc',
            name='players',
            field=models.ManyToManyField(blank=True, null=True, to='main.players'),
        ),
        migrations.AlterField(
            model_name='fc',
            name='stadium',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.stadium'),
        ),
        migrations.AlterField(
            model_name='fc',
            name='staff',
            field=models.ManyToManyField(blank=True, null=True, to='main.staff'),
        ),
        migrations.AlterField(
            model_name='game',
            name='guest_action',
            field=models.ManyToManyField(related_name='guest', to='main.action'),
        ),
        migrations.AlterField(
            model_name='game',
            name='host_action',
            field=models.ManyToManyField(related_name='host', to='main.action'),
        ),
        migrations.AlterField(
            model_name='players',
            name='position',
            field=models.IntegerField(choices=[(4, 'goalkeeper'), (2, 'midfielder'), (3, 'defender'), (1, 'forward')], default=1),
        ),
        migrations.AlterField(
            model_name='preview',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest', to='main.fc'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.IntegerField(choices=[(3, 'physiotherapist'), (1, 'trainer'), (4, 'doctor'), (6, 'admin'), (2, 'sub-trainer'), (5, 'goalkeeper-trainer')]),
        ),
        migrations.DeleteModel(
            name='Club',
        ),
        migrations.DeleteModel(
            name='GuestAction',
        ),
    ]
