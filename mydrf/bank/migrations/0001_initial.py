# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('accountid', models.AutoField(serialize=False, primary_key=True)),
                ('credit', models.CharField(max_length=100)),
                ('debit', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
                ('crediton', models.DateTimeField(default=datetime.datetime.now)),
                ('debiton', models.DateTimeField(default=datetime.datetime.now)),
                ('lasttransactionon', models.DateTimeField(default=datetime.datetime.now)),
                ('createdon', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='customers',
            fields=[
                ('customerid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('createdon', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='account',
            name='customerid',
            field=models.ForeignKey(to='bank.customers'),
            preserve_default=True,
        ),
    ]
