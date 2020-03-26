# Generated by Django 2.0.7 on 2020-03-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tempm14expl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_no', models.CharField(blank=True, db_column='PART_NO', max_length=8, null=True)),
                ('qty', models.DecimalField(blank=True, db_column='QTY', decimal_places=3, max_digits=9, null=True)),
                ('ptc', models.CharField(blank=True, db_column='PTC', max_length=1, null=True)),
                ('rm_partno', models.CharField(blank=True, db_column='RM_PARTNO', max_length=8, null=True)),
                ('rm_qty', models.DecimalField(blank=True, db_column='RM_QTY', decimal_places=3, max_digits=8, null=True)),
                ('rm_ptc', models.CharField(blank=True, db_column='RM_PTC', max_length=1, null=True)),
            ],
        ),
    ]
