# Generated by Django 2.1.7 on 2019-04-30 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_merge_20190430_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='item',
        ),
        migrations.RemoveField(
            model_name='item',
            name='author',
        ),
        migrations.RemoveField(
            model_name='item',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
