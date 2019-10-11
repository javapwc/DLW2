# Generated by Django 2.0.7 on 2019-10-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0024_auto_20191010_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='m14m4',
            name='closing_bal14',
            field=models.CharField(blank=True, db_column='CLOSING_BAL14', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='m14m4',
            name='issued_qty14',
            field=models.CharField(blank=True, db_column='ISSUED_QTY14', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='m14m4',
            name='laser_pst14',
            field=models.CharField(blank=True, db_column='LASER_PST14', default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='m14m4',
            name='line14',
            field=models.CharField(blank=True, db_column='LINE14', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='m14m4',
            name='posted1_date14',
            field=models.CharField(blank=True, db_column='POSTED1_DATE14', default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='m14m4',
            name='posted_date14',
            field=models.CharField(blank=True, db_column='POSTED_DATE14', default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='m14m4',
            name='received_mat14',
            field=models.CharField(blank=True, db_column='RECEIVED_MAT14', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='m14m4',
            name='received_qty14',
            field=models.CharField(blank=True, db_column='RECEIVED_QTY14', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='m14m4',
            name='remarks14',
            field=models.CharField(blank=True, db_column='REMARKS14', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='m14m4',
            name='shopsup_date14',
            field=models.CharField(blank=True, db_column='SHOPSUP_DATE14', default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='m14m4',
            name='wardkp_date14',
            field=models.CharField(blank=True, db_column='WARDKP_DATE14', default=0, max_length=50),
        ),
    ]