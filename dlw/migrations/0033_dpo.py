# Generated by Django 2.0.7 on 2019-10-11 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlw', '0032_pinionpressing'),
    ]

    operations = [
        migrations.CreateModel(
            name='dpo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loconame', models.CharField(max_length=50, null=True)),
                ('locotype', models.CharField(max_length=50, null=True)),
                ('endcumno', models.CharField(max_length=10, null=True)),
                ('orderno', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
