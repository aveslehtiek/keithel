# Generated by Django 3.1.2 on 2020-11-06 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_product_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]