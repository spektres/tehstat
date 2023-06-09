# Generated by Django 4.0.5 on 2022-07-05 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desktop', '0001_initial'),
        ('service', '0004_alter_history_request_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history_request',
            name='compressor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='desktop.compressor', verbose_name='Компрессор'),
        ),
        migrations.AlterField(
            model_name='history_request',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='desktop.room', verbose_name='Помещение'),
        ),
        migrations.AlterField(
            model_name='history_request',
            name='text_close',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Решение проблемы'),
        ),
        migrations.AlterField(
            model_name='history_request',
            name='text_open',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Возникшая проблема'),
        ),
    ]
