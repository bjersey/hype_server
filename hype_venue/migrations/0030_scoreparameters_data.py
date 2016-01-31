# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0029_remove_scoreparameters_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoreparameters',
            name='data',
            field=django_hstore.fields.DictionaryField(null=True, blank=True),
        ),
    ]
