# Generated by Django 3.0.8 on 2020-08-14 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_auto_20200812_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='watch_list',
            name='al_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing', to='auctions.Auction_listing'),
        ),
        migrations.AlterField(
            model_name='watch_list',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
