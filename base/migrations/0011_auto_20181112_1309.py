# Generated by Django 2.1.2 on 2018-11-12 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20181112_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('depends', 'Depends on')], max_length=20)),
                ('from_resource', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_resource', to='base.Resource')),
                ('to_resource', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='to_resource', to='base.Resource')),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='relation',
            field=models.ManyToManyField(through='base.Relationship', to='base.Resource'),
        ),
    ]
