# Generated by Django 2.2 on 2019-04-05 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=300, null=True)),
                ('date_subscribed', models.DateField(default=datetime.date.today)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
