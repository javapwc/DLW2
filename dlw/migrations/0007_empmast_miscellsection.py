# Generated by Django 2.0.7 on 2019-10-09 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0006_barrelfirst'),
    ]

    operations = [
        migrations.CreateModel(
            name='empmast',
            fields=[
                ('empno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=50, null=True)),
                ('birthdate', models.CharField(max_length=50, null=True)),
                ('sex', models.CharField(max_length=10, null=True)),
                ('marital_status', models.CharField(max_length=10, null=True)),
                ('decode_paycategory', models.CharField(max_length=50, null=True)),
                ('billunit', models.CharField(max_length=50, null=True)),
                ('service_status', models.CharField(max_length=50, null=True)),
                ('emp_status', models.CharField(max_length=50, null=True)),
                ('rectt_category', models.CharField(max_length=50, null=True)),
                ('payband', models.CharField(max_length=10, null=True)),
                ('scalecode', models.CharField(max_length=50, null=True)),
                ('pc7_level', models.CharField(max_length=10, null=True)),
                ('payrate', models.CharField(max_length=50, null=True)),
                ('office', models.CharField(max_length=50, null=True)),
                ('station_des', models.CharField(max_length=50, null=True)),
                ('emptype', models.CharField(max_length=10, null=True)),
                ('medicalcode', models.CharField(max_length=50, null=True)),
                ('tradecode', models.CharField(max_length=50, null=True)),
                ('dept_desc', models.CharField(max_length=50, null=True)),
                ('parentshop', models.CharField(max_length=50, null=True)),
                ('shopno', models.CharField(max_length=50, null=True)),
                ('desig_longdesc', models.CharField(max_length=50, null=True)),
                ('wau', models.CharField(max_length=50, null=True)),
                ('inc_category', models.CharField(max_length=50, null=True)),
                ('emp_inctype', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MiscellSection',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('bo_no', models.CharField(max_length=20, null=True)),
                ('bo_date', models.CharField(max_length=20, null=True)),
                ('shaft_m', models.CharField(max_length=20, null=True)),
                ('in_qty', models.IntegerField(null=True)),
                ('out_qty', models.IntegerField(null=True)),
                ('date', models.CharField(max_length=20, null=True)),
                ('loco_type', models.CharField(max_length=20, null=True)),
                ('dispatch_to', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]