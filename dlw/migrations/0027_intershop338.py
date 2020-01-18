# Generated by Django 2.0.7 on 2020-01-18 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0026_delete_intershop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intershop338',
            fields=[
                ('shop_sec', models.CharField(blank=True, db_column='SHOP_SEC', default=0, max_length=50, null=True)),
                ('staffNo', models.CharField(db_column='STAFF_NO', max_length=20, primary_key=True, serialize=False)),
                ('staffName', models.CharField(db_column='STAFF_NAME', max_length=50, null=True)),
                ('staffDesg', models.CharField(db_column='STAFF_DESG', max_length=50, null=True)),
                ('reference_authority', models.CharField(db_column='REFERENCE_AUTHORITY', max_length=100, null=True)),
                ('staffRate', models.CharField(blank=True, db_column='STAFF_RATE', max_length=50, null=True)),
                ('toshop_sec', models.CharField(blank=True, db_column='TOSHOP_SEC', default=0, max_length=50, null=True)),
                ('date1', models.DateField(db_column='DATE1', max_length=20, null=True)),
                ('login_id', models.CharField(blank=True, db_column='LOGIN_ID', max_length=10, null=True)),
                ('status', models.CharField(blank=True, db_column='STATUS', max_length=5, null=True)),
                ('current_date', models.DateTimeField(blank=True, db_column='CURRENT_DATE', null=True)),
            ],
        ),
    ]
