# Generated by Django 2.0.3 on 2018-04-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.TextField(default='', max_length=10000)),
                ('example', models.TextField(default='', max_length=10000)),
                ('hit', models.IntegerField(max_length=10000)),
            ],
        ),
    ]
