# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-20 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_notes_note_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
    ]