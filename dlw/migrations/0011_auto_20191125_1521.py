# Generated by Django 2.0.7 on 2019-11-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0010_mg9initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='axlemachining',
            name='in_qty',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='axlemachining',
            name='out_qty',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='axlewheelpressing',
            name='in_qty',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='axlewheelpressing',
            name='out_qty',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='bogieassembly',
            name='in_qty',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='bogieassembly',
            name='out_qty',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='wheelmachining',
            name='in_qty',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='wheelmachining',
            name='out_qty',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='miscellsection',
            name='in_qty',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='miscellsection',
            name='out_qty',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
