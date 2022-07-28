# Generated by Django 3.2.14 on 2022-07-28 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20220728_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order_status',
            field=models.CharField(choices=[('P', 'Pending Payment'), ('T', 'Out for Delivery'), ('D', 'Delivered')], default='Pending Payment', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
