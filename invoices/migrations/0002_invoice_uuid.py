# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import uuid

def add_uuids(apps, schema_editor):
    Invoice = apps.get_model("invoices", "Invoice")
    
    for invoice in Invoice.objects.all():
        invoice.uuid = uuid.uuid4()
        invoice.save()

class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='uuid',
            field=models.UUIDField(default=None, editable=False, unique=False, null=True),
        ),
        migrations.RunPython(add_uuids, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='invoice',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
        )
    ]