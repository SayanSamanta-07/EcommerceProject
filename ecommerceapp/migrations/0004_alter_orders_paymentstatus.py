# Generated by Django 5.0.1 on 2024-01-29 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0003_orders_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='paymentstatus',
            field=models.CharField(default='Cash on Delivery', max_length=50),
        ),
    ]