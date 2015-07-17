# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formflow', '0002_auto_20150717_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flow',
            name='currentForm',
            field=models.OneToOneField(related_name='flow_currentForm', null=True, blank=True, to='formflow.Form'),
        ),
    ]
