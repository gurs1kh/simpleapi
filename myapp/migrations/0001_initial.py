# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('publisher', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('link', models.CharField(max_length=2083)),
                ('cover', models.CharField(max_length=2083)),
            ],
        ),
    ]
