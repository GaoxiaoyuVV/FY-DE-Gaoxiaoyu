# Generated by Django 2.0.3 on 2018-04-23 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20180423_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='hit',
        ),
    ]