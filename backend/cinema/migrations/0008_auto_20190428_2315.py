# Generated by Django 2.2 on 2019-04-28 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0007_auto_20190427_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='length',
            field=models.IntegerField(default=4, max_length=99),
        ),
        migrations.AddField(
            model_name='hall',
            name='width',
            field=models.IntegerField(default=5, max_length=99),
        ),
    ]
