# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('locations', models.TextField()),
                ('category', models.CharField(max_length=200)),
                ('mission_statement', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='organization',
            field=models.ForeignKey(null=True, blank=True, to='api.Organization'),
        ),
    ]
