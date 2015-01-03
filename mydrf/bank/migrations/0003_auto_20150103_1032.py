# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20150103_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='crediton',
        ),
        migrations.RemoveField(
            model_name='account',
            name='debiton',
        ),
    ]
