# Generated by Django 2.2.2 on 2019-06-22 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190622_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]