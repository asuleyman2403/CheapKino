# Generated by Django 2.2 on 2019-04-27 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_auto_20190427_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='row',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.Hall'),
        ),
    ]
