# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='lastMaintenanceDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 1, 19, 44, 48, 369438, tzinfo=utc), verbose_name='Last Maintenance Conducted'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='lastMaintenanceJob',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equipment',
            name='maintenanceSchedule',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equipment',
            name='nextMaintenanceDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 1, 19, 45, 0, 985160, tzinfo=utc), verbose_name='Next Maintenance Job'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='nextMaintenanceJob',
            field=models.IntegerField(default=0),
        ),
    ]
