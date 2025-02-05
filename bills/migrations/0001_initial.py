# Generated by Django 5.0.6 on 2024-05-21 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
        ("cart", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "shipping_address",
                    models.CharField(max_length=50, verbose_name="shipping address"),
                ),
                (
                    "billing_address",
                    models.CharField(max_length=50, verbose_name="billling address"),
                ),
                ("has_paid", models.BooleanField(verbose_name="has paid")),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("ESEWA", "Esewa"),
                            ("COD", "Cash On Delivery"),
                            ("KHALTI", "Khalti"),
                            ("BANK TRANSFER", "Bank Transfer"),
                        ],
                        max_length=50,
                        verbose_name="Payment Method",
                    ),
                ),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cart.cart",
                        verbose_name="cart",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.customer",
                        verbose_name="customer",
                    ),
                ),
            ],
            options={
                "verbose_name": "Bill",
                "verbose_name_plural": "Billings",
            },
        ),
    ]
