# Generated by Django 2.0.7 on 2019-10-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0023_auto_20191010_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m5shemp',
            name='staff_no',
            field=models.CharField(blank=True, db_column='STAFF_NO', max_length=50, null=True),
        ),
    ]
