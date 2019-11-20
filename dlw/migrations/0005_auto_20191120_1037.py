# Generated by Django 2.0.7 on 2019-11-20 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0004_mg36'),
    ]

    operations = [
        migrations.CreateModel(
            name='exam_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_code', models.CharField(blank=True, max_length=10, null=True)),
                ('prac_desc', models.CharField(blank=True, max_length=500, null=True)),
                ('oral_desc', models.CharField(blank=True, max_length=500, null=True)),
                ('exam_type', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='mg33new',
            name='oral_desc',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='mg33new',
            name='prac_desc',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
