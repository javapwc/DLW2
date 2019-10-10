# Generated by Django 2.0.7 on 2019-10-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0011_remove_m14m4_epc_old1'),
    ]

    operations = [
        migrations.AddField(
            model_name='m14m4',
            name='closing_bal',
            field=models.CharField(blank=True, db_column='CLOSING_BAL', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='m14m4',
            name='issued_qty',
            field=models.CharField(blank=True, db_column='ISSUED_QTY', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='m14m4',
            name='line',
            field=models.CharField(blank=True, db_column='LINE', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='m14m4',
            name='received_mat',
            field=models.CharField(blank=True, db_column='REC_MAT', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='m14m4',
            name='received_qty',
            field=models.CharField(blank=True, db_column='REC_QTY', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='m14m4',
            name='remarks',
            field=models.CharField(blank=True, db_column='REMARKS', max_length=50, null=True),
        ),
    ]
