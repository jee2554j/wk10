# Generated by Django 2.2 on 2019-04-28 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190428_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='shop.Tag'),
        ),
    ]
