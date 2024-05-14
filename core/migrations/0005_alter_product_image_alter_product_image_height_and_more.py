# Generated by Django 5.0.6 on 2024-05-13 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, height_field='image_height', null=True, upload_to='images/products/', verbose_name='image', width_field='image_width'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_height',
            field=models.IntegerField(default=1080),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_width',
            field=models.IntegerField(default=1080),
        ),
    ]