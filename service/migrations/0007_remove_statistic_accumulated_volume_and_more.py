# Generated by Django 4.2.2 on 2023-07-11 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_history_request_air_assembly_shut_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistic',
            name='accumulated_volume',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='fan_starts',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='load_relay',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='number_of_starts',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='regulator_hours',
        ),
    ]