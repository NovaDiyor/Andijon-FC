# Generated by Django 4.1 on 2022-11-09 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_productimage_images_alter_players_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='position',
            field=models.IntegerField(choices=[(2, 'midfielder'), (3, 'defender'), (1, 'forward'), (4, 'goalkeeper')], default=1),
        ),
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('match_day', models.IntegerField()),
                ('team', models.ManyToManyField(to='main.players')),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('squad_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.squad')),
                ('team', models.ManyToManyField(to='main.players')),
            ],
        ),
    ]