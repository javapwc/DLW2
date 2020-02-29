# Generated by Django 2.0.7 on 2020-02-29 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='m18',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopIncharge', models.CharField(blank=True, db_column='SHOPINCHARGE', default=0, max_length=100, null=True)),
                ('shop_sec', models.CharField(blank=True, db_column='SHOPSEC', default=0, max_length=50, null=True)),
                ('wo_no', models.CharField(blank=True, db_column='WONO', default=0, max_length=50, null=True)),
                ('part_nop', models.CharField(blank=True, db_column='PARTNOP', max_length=50, null=True)),
                ('extraTimePartNo', models.CharField(blank=True, db_column='EXTRATIMEPARTNO', max_length=100, null=True)),
                ('reasonSpecialAllowance', models.CharField(blank=True, db_column='REASON_SPCL_ALLOW', max_length=300, null=True)),
                ('forSpecialAllowance', models.CharField(blank=True, db_column='FOR_SPCL_ALLOW', max_length=300, null=True)),
                ('totalExtraTime', models.CharField(blank=True, db_column='TOTAL_EXTRA_TIME', max_length=100, null=True)),
                ('opno', models.CharField(blank=True, db_column='OPNO', max_length=100, null=True)),
                ('opdesc', models.CharField(blank=True, db_column='OPDESC', max_length=300, null=True)),
                ('discription', models.CharField(blank=True, db_column='DISCRIPTION', max_length=300, null=True)),
                ('quantity', models.CharField(blank=True, db_column='QUANTITY', max_length=100, null=True)),
                ('setExtraTime', models.CharField(blank=True, db_column='SET_EXTRA_TIME', max_length=200, null=True)),
                ('setno', models.CharField(blank=True, db_column='SETNO', max_length=100, null=True)),
                ('refNo', models.CharField(blank=True, db_column='REFNO', max_length=100, null=True)),
                ('proReason', models.CharField(blank=True, db_column='PROBABLE REASON', max_length=100, null=True)),
            ],
        ),
    ]
