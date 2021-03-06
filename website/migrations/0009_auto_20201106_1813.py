# Generated by Django 3.1.2 on 2020-11-06 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20201106_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='payment_method',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='service_area',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
