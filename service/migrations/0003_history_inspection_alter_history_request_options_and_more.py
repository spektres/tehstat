# Generated by Django 4.0.5 on 2022-06-20 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('desktop', '0001_initial'),
        ('service', '0002_history_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='History_inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_ok', models.BooleanField(default=True)),
                ('mehanical_assembly', models.BooleanField(default=False)),
                ('mehanical_assembly_text', models.CharField(blank=True, max_length=200, null=True)),
                ('electrical_assembly', models.BooleanField(default=False)),
                ('electrical_assembly_text', models.CharField(blank=True, max_length=200, null=True)),
                ('oil_assembly', models.BooleanField(default=False)),
                ('oil_assembly_text', models.CharField(blank=True, max_length=200, null=True)),
                ('air_assembly', models.BooleanField(default=False)),
                ('air_assembly_text', models.CharField(blank=True, max_length=200, null=True)),
                ('another', models.BooleanField(default=False)),
                ('another_text', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('compressor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='desktop.compressor')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='desktop.room')),
            ],
            options={
                'verbose_name': 'История осмотра',
                'verbose_name_plural': 'История осмотра',
                'ordering': ['-created_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='history_request',
            options={'ordering': ['-created_date'], 'verbose_name': 'История статистики', 'verbose_name_plural': 'История статистики'},
        ),
        migrations.DeleteModel(
            name='History',
        ),
    ]
