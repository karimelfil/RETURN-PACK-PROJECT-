# Generated by Django 5.0.6 on 2024-06-10 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('returnpack', '0004_alter_packaging_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagingmouvment',
            name='packaging',
        ),
    ]
