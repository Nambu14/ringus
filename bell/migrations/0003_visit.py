# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bell', '0002_auto_20150915_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'Fecha de Visita')),
                ('idVisitor', models.ForeignKey(to='bell.Visitor')),
            ],
        ),
    ]
