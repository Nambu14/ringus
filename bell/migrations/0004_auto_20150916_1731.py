# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bell', '0003_visit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='visitorId',
            new_name='visitor',
        ),
        migrations.RenameField(
            model_name='visit',
            old_name='idVisitor',
            new_name='visitor',
        ),
    ]
