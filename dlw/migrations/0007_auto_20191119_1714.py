# Generated by Django 2.0.7 on 2019-11-19 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0006_mg33exammaster'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mg33new',
            old_name='acc_date',
            new_name='exam_date',
        ),
        migrations.RemoveField(
            model_name='mg33new',
            name='oral_desc',
        ),
        migrations.RemoveField(
            model_name='mg33new',
            name='place',
        ),
        migrations.RemoveField(
            model_name='mg33new',
            name='prac_desc',
        ),
    ]