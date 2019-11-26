# Generated by Django 2.0.7 on 2019-11-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0009_auto_20191124_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='MG9Initial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec', models.CharField(blank=True, db_column='SEC', max_length=4, null=True)),
                ('mw_no', models.CharField(blank=True, db_column='MW_NO', max_length=4, null=True)),
                ('staff_no', models.CharField(blank=True, db_column='STAFF_NO', max_length=5, null=True)),
                ('complaint', models.CharField(blank=True, db_column='COMPLAINT', max_length=70, null=True)),
                ('handed_date', models.CharField(blank=True, db_column='HANDED_DATE', max_length=10, null=True)),
                ('comp_date', models.CharField(blank=True, db_column='COMP_DATE', max_length=10, null=True)),
                ('handed_time', models.CharField(blank=True, db_column='HANDED_TIME', max_length=10, null=True)),
                ('comp_time', models.CharField(blank=True, db_column='COMP_TIME', max_length=10, null=True)),
                ('handed_cmsec', models.CharField(blank=True, db_column='HANDED_CMSEC', max_length=20, null=True)),
                ('comp_cmsec', models.CharField(blank=True, db_column='COMP_CMSEC', max_length=20, null=True)),
                ('handed_cmserv', models.CharField(blank=True, db_column='HANDED_CMSERV', max_length=20, null=True)),
                ('comp_cmserv', models.CharField(blank=True, db_column='COMP_CMSERV', max_length=20, null=True)),
                ('action', models.CharField(blank=True, db_column='ACTION', max_length=20, null=True)),
                ('sl_no', models.CharField(blank=True, db_column='SL_NO', max_length=5, null=True)),
                ('last_modified', models.CharField(blank=True, db_column='LAST_MODIFIED', max_length=50, null=True)),
                ('login_id', models.CharField(blank=True, db_column='LOGIN_ID', max_length=15, null=True)),
            ],
            options={
                'db_table': 'MG9Initial',
            },
        ),
    ]