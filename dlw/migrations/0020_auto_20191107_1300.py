# Generated by Django 2.0.7 on 2019-11-07 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0019_bogieassembly_elastic_shop_make'),
    ]

    operations = [
        migrations.RenameField(
            model_name='axlewheelpressing',
            old_name='inspection_status',
            new_name='axleinspection_status',
        ),
        migrations.AddField(
            model_name='axlewheelpressing',
            name='wheelinspection_status',
            field=models.NullBooleanField(),
        ),
    ]