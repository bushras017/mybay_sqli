# Generated by Django 3.0.8 on 2020-08-16 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_auto_20200816_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listing',
            name='bidders_count',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='auction_listing',
            name='watchers_count',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
