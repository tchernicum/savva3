# Generated by Django 2.1.2 on 2018-11-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField()),
            ],
        ),
    ]
