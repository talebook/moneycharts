# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 00:19
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.CharField(default=b'', max_length=16, primary_key=True, serialize=False, unique=True)),
                ('type', models.IntegerField(default=Decimal('0'))),
                ('name', models.CharField(default=b'', max_length=128)),
                ('date', models.DateTimeField()),
                ('balance', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('tax', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('fee1', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('fee2', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('fee3', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('stock_name', models.CharField(default=b'', max_length=16)),
                ('stock_code', models.CharField(default=b'', max_length=16)),
                ('stock_price', models.IntegerField(default=Decimal('0'))),
                ('stock_num', models.IntegerField(default=Decimal('0'))),
                ('stock_money', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('account', models.CharField(default=b'', max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('low', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('high', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('open', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('close', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('base', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('money', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('balance', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stocks_num', models.IntegerField(default=Decimal('0'))),
                ('stocks_raw', models.TextField(default=b'')),
                ('stocks_val', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('base', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('free', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=19)),
                ('is_outdate', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SimpleCache',
            fields=[
                ('key', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('val', models.TextField(default=b'')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='node',
            unique_together=set([('user', 'type', 'date')]),
        ),
    ]
