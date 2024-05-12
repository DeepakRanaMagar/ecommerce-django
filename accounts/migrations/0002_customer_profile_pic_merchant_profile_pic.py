# Generated by Django 5.0.6 on 2024-05-12 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/customer%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='merchant',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/merchant%Y/%m/%d/'),
        ),
    ]
