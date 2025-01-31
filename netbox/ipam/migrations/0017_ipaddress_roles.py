# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 19:37
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0016_unicode_literals'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipaddress',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, 'Loopback'), (20, 'Secondary'), (30, 'Anycast'), (40, 'VIP'), (41, 'VRRP'), (42, 'HSRP'), (43, 'GLBP'), (50, 'BGP P2P')], help_text='The functional role of this IP', null=True, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Active'), (2, 'Reserved'), (3, 'Deprecated'), (5, 'DHCP')], default=1, help_text='The operational status of this IP', verbose_name='Status'),
        ),
    ]
