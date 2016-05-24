# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hype_core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hype_beacon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVisit',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='hype_core.TimeStampedModel')),
                ('beacon', models.ForeignKey(to='hype_beacon.Beacon')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            bases=('hype_core.timestampedmodel',),
        ),
    ]
