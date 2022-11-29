# Generated by Django 4.0.6 on 2022-11-29 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_collection_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='collection_date',
            field=models.DateField(choices=[(datetime.date(2022, 11, 30), 'Wed: Nov 30'), (datetime.date(2022, 12, 1), 'Thu: Dec 01'), (datetime.date(2022, 12, 2), 'Fri: Dec 02'), (datetime.date(2022, 12, 3), 'Sat: Dec 03'), (datetime.date(2022, 12, 4), 'Sun: Dec 04'), (datetime.date(2022, 12, 5), 'Mon: Dec 05'), (datetime.date(2022, 12, 6), 'Tue: Dec 06'), (datetime.date(2022, 12, 7), 'Wed: Dec 07')], null=True),
        ),
    ]
