# Generated by Django 3.1.2 on 2020-11-12 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20201112_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
