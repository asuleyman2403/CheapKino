# Generated by Django 2.2 on 2019-05-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0008_auto_20190427_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='status',
        ),
        migrations.AlterField(
            model_name='session',
            name='price_child',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='session',
            name='price_student',
            field=models.IntegerField(),
        ),
    ]
