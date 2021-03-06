# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-20 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='choice_text',
            new_name='note_text',
        ),
        migrations.AddField(
            model_name='notes',
            name='_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.Classes'),
        ),
        migrations.AddField(
            model_name='notes',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
    ]
