# Generated by Django 2.0.7 on 2019-10-17 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0002_auto_20191016_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='m20new',
            old_name='date',
            new_name='alt_date',
        ),
        migrations.RemoveField(
            model_name='m20new',
            name='sno',
        ),
        migrations.AddField(
            model_name='m20new',
            name='lv_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='m20new',
            name='staff_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]