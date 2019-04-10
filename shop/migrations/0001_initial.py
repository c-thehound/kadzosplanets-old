# Generated by Django 2.2 on 2019-04-02 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('amount_in_stock', models.IntegerField()),
            ],
        ),
    ]
