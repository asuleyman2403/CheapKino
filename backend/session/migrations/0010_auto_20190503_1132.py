# Generated by Django 2.2 on 2019-05-03 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0009_auto_20190503_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='cinema.Hall'),
        ),
        migrations.AlterField(
            model_name='session',
            name='price_child',
            field=models.IntegerField(default=models.IntegerField()),
        ),
        migrations.AlterField(
            model_name='session',
            name='price_student',
            field=models.IntegerField(default=models.IntegerField()),
        ),
    ]
