# Generated by Django 2.0.7 on 2020-05-27 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0006_qtysumtemp_qtysumtemp1_qtysumtemp2'),
    ]

    operations = [
        migrations.AddField(
            model_name='empmast',
            name='op_create',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='empmast',
            name='op_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='empmast',
            name='op_read',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='empmast',
            name='op_update',
            field=models.BooleanField(default=False),
        ),
    ]
