# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-09 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('braintreepayment', '0002_payment_refactor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='braintreetransaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]