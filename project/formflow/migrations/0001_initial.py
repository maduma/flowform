# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=16, choices=[(b'DATE', b'DATE'), (b'EMAIL', b'EMAIL'), (b'NAME', b'NAME')])),
                ('value', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('action', models.CharField(max_length=16, choices=[(b'NEXT', b'NEXT'), (b'PREV', b'PREV'), (b'SUMMARY', b'SUMMARY'), (b'SEND', b'SEND')])),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=16, choices=[(b'SIMPLE', b'SIMPLE'), (b'ARRAY', b'ARRAY')])),
                ('flow', models.ForeignKey(to='formflow.Flow')),
            ],
        ),
        migrations.AddField(
            model_name='flow',
            name='currentForm',
            field=models.OneToOneField(related_name='flow_currentForm', to='formflow.Form'),
        ),
        migrations.AddField(
            model_name='field',
            name='form',
            field=models.ForeignKey(to='formflow.Form'),
        ),
    ]
