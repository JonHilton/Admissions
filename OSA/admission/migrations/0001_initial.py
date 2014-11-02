# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pt_first_name', models.CharField(max_length=30)),
                ('pt_last_name', models.CharField(max_length=30)),
                ('time_added', models.DateTimeField(verbose_name=b'time added')),
                ('pt_number', models.CharField(max_length=7)),
                ('pt_dob', models.DateField(verbose_name=b'date of birth')),
                ('presenting_condition', models.CharField(max_length=200)),
                ('senior_review', models.CharField(default=b'None', max_length=4, choices=[(b'ER', b'Dr Russell'), (b'JS', b'Dr Stosic'), (b'AB', b'Dr Blackburn'), (b'MV', b'Dr Venu'), (b'None', b'None yet')])),
                ('origin', models.CharField(default=b'GP', max_length=2, choices=[(b'ED', b'Emergency Department'), (b'GP', b'By their GP')])),
                ('clerked_by', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=20)),
                ('jobs', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
