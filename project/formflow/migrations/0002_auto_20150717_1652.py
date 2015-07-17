# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flow',
            name='action',
            field=models.CharField(default=b'NEXT', max_length=16, choices=[(b'NEXT', b'NEXT'), (b'PREV', b'PREV'), (b'SUMMARY', b'SUMMARY'), (b'SEND', b'SEND')]),
        ),
        migrations.AlterField(
            model_name='flow',
            name='currentForm',
            field=models.OneToOneField(related_name='flow_currentForm', null=True, to='formflow.Form'),
        ),
    ]
