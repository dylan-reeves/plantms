# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_auto_20151101_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='nextMaintenanceDate',
        ),
        migrations.AddField(
            model_name='equipment',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='nextMaintenanceScheduled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='equipment',
            name='nextMaintenanceWindowEndDate',
            field=models.DateField(null=True, blank=True, verbose_name='Next Maintenance Window Close'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='nextMaintenanceWindowStartDate',
            field=models.DateField(null=True, blank=True, verbose_name='Next Maintenance Window Open'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='lastMaintenanceDate',
            field=models.DateField(null=True, blank=True, verbose_name='Last Maintenance Conducted'),
        ),
    ]
