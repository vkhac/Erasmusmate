# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 15:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hardworking', models.CharField(choices=[('Absolutely', 'Absolutely'), ('A bit', 'A bit'), ("Don't care", "Don't care"), ('Not really', 'Not really'), ('Absolutely not', 'Absolutely not')], default="Don't care", max_length=20)),
                ('partying', models.CharField(choices=[('Absolutely', 'Absolutely'), ('A bit', 'A bit'), ("Don't care", "Don't care"), ('Not really', 'Not really'), ('Absolutely not', 'Absolutely not')], default="Don't care", max_length=20)),
                ('traveling', models.CharField(choices=[('Absolutely', 'Absolutely'), ('A bit', 'A bit'), ("Don't care", "Don't care"), ('Not really', 'Not really'), ('Absolutely not', 'Absolutely not')], default="Don't care", max_length=20)),
                ('price', models.PositiveIntegerField(default=0)),
                ('smoking_permitted', models.CharField(choices=[("Don't care", "Don't care"), ('Yes', 'Yes'), ('No', 'No')], default="Don't care", max_length=10)),
                ('same_nationality_roommates', models.CharField(choices=[("Don't care", "Don't care"), ('Yes', 'Yes'), ('No', 'No')], default="Don't care", max_length=10)),
                ('time_of_staying_in_flat', models.CharField(choices=[('UNKNOWN', 'UNKNOWN'), ('1 MONTH', '1 MONTH'), ('2 MONTHS', '2 MONTHS'), ('3 MONTHS', '3 MONTHS'), ('4 MONTHS', '4 MONTHS'), ('5 MONTHS ', '5 MONTHS'), ('6 MONTHS ', '6 MONTHS')], default='UNKNOWN', max_length=10)),
                ('men_or_women_on_room', models.CharField(choices=[("Don't care", "Don't care"), ('Men only', 'Men only'), ('Women only', 'Women only')], default="Don't care", max_length=10)),
                ('num_of_roommates', models.CharField(choices=[("Don't care", "Don't care"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default="Don't care", max_length=10)),
                ('age', models.PositiveIntegerField(blank=True, default=0)),
                ('sex', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='', max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField(blank=True, default=0)),
                ('country_of_origin', models.CharField(blank=True, default='', max_length=20)),
                ('country_of_studies', models.CharField(blank=True, default='', max_length=20)),
                ('city_of_studies', models.CharField(blank=True, default='', max_length=20)),
                ('region', models.CharField(blank=True, default='', max_length=20)),
                ('university', models.CharField(blank=True, default='', max_length=20)),
                ('faculty', models.CharField(blank=True, default='', max_length=30)),
                ('prefered_cuisine', models.CharField(choices=[('GR', 'GREEK'), ('FR', 'FRENCH'), ('CHINESE', 'CHINESE'), ('INTERNATIONAL', 'INTERNATIONAL')], default='', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
