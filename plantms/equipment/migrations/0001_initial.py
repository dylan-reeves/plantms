# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
from django.conf import settings
import audit_log.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('created_by', audit_log.models.fields.CreatingUserField(verbose_name='created by', editable=False, to=settings.AUTH_USER_MODEL, related_name='created_equipment_department_set', null=True)),
                ('modified_by', audit_log.models.fields.LastUserField(verbose_name='modified by', editable=False, to=settings.AUTH_USER_MODEL, related_name='modified_equipment_department_set', null=True)),
                ('reportingManager', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('intervalType', models.CharField(max_length=100)),
                ('created_by', audit_log.models.fields.CreatingUserField(verbose_name='created by', editable=False, to=settings.AUTH_USER_MODEL, related_name='created_equipment_equipment_set', null=True)),
                ('department', models.ForeignKey(to='equipment.department')),
                ('modified_by', audit_log.models.fields.LastUserField(verbose_name='modified by', editable=False, to=settings.AUTH_USER_MODEL, related_name='modified_equipment_equipment_set', null=True)),
            ],
            options={
                'abstract': False,
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('created_by', audit_log.models.fields.CreatingUserField(verbose_name='created by', editable=False, to=settings.AUTH_USER_MODEL, related_name='created_equipment_site_set', null=True)),
                ('modified_by', audit_log.models.fields.LastUserField(verbose_name='modified by', editable=False, to=settings.AUTH_USER_MODEL, related_name='modified_equipment_site_set', null=True)),
                ('reportingUsers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
            },
        ),
        migrations.AddField(
            model_name='equipment',
            name='site',
            field=models.ForeignKey(to='equipment.site'),
        ),
        migrations.AddField(
            model_name='department',
            name='sites',
            field=models.ManyToManyField(to='equipment.site'),
        ),
    ]
