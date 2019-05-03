# Generated by Django 2.2 on 2019-05-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20190503_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]