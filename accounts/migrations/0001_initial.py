# Generated by Django 5.0.6 on 2024-05-14 12:17

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/customer%Y/%m/%d/')),
                ('dob', models.DateField(verbose_name='date of birth')),
                ('address1', models.CharField(blank=True, max_length=150, null=True)),
                ('address2', models.CharField(blank=True, max_length=150, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/merchant%Y/%m/%d/')),
                ('merchant_name', models.CharField(max_length=50, verbose_name='merchant name')),
                ('pan_no', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999)], verbose_name='Pan No')),
                ('address1', models.CharField(blank=True, max_length=150, null=True)),
                ('address2', models.CharField(blank=True, max_length=150, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
        ),
    ]
