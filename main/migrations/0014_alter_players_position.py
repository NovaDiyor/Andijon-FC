# Generated by Django 4.1 on 2022-11-09 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_region_remove_order_province_remove_order_town_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='position',
            field=models.IntegerField(choices=[(1, 'forward'), (2, 'midfielder'), (4, 'goalkeeper'), (3, 'defender')], default=1),
        ),
    ]