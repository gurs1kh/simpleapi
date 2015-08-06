# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='author',
            new_name='authors',
        ),
        migrations.AlterField(
            model_name='books',
            name='pub_date',
            field=models.CharField(max_length=20),
        ),
    ]
