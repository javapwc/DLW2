# Generated by Django 2.0.7 on 2019-12-06 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0017_staff_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='rates',
            name='staff_no',
            field=models.CharField(blank=True, db_column='STAFF_NO', max_length=10, null=True),
        ),
    ]