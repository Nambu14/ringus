# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bell', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='VisitorId',
            new_name='visitorId',
        ),
    ]
