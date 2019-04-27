# Generated by Django 2.2 on 2019-04-27 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0004_auto_20190427_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='row',
        ),
        migrations.AlterField(
            model_name='seatreserve',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserved', to='cinema.Seat'),
        ),
        migrations.DeleteModel(
            name='Row',
        ),
        migrations.DeleteModel(
            name='Seat',
        ),
    ]
