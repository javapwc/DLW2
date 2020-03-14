# Generated by Django 2.0.7 on 2020-03-14 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0002_m18'),
    ]

    operations = [
        migrations.CreateModel(
            name='roster1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_sec', models.CharField(blank=True, db_column='shop_sec', max_length=20, null=True)),
                ('staffNo', models.CharField(blank=True, db_column='staffNo', max_length=20, null=True)),
                ('staffName', models.CharField(blank=True, db_column='staffName', max_length=100, null=True)),
                ('shift', models.CharField(blank=True, db_column='shift', max_length=20, null=True)),
                ('date', models.CharField(blank=True, db_column='date', max_length=10, null=True)),
            ],
        ),
    ]