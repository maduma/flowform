# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formflow', '0003_auto_20150717_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='field',
            name='value',
        ),
        migrations.AlterField(
            model_name='flow',
            name='action',
            field=models.CharField(default=b'NONE', max_length=16, choices=[(b'NONE', b'NONE'), (b'NEXT', b'NEXT'), (b'PREV', b'PREV'), (b'SUMMARY', b'SUMMARY'), (b'SEND', b'SEND')]),
        ),
    ]
