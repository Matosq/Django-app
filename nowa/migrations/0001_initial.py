# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Tytuł', max_length=150)),
                ('content', models.TextField(verbose_name='Zawartość')),
                ('published', models.DateTimeField(verbose_name='Data publikacji')),
            ],
        ),
    ]
