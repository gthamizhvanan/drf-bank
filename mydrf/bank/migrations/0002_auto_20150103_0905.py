# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='credit',
            field=models.CharField(default=0, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='customerid',
            field=models.ForeignKey(related_name='accounts', to='bank.customers'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='debit',
            field=models.CharField(default=0, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='total',
            field=models.CharField(default=0, max_length=100),
            preserve_default=True,
        ),
    ]
