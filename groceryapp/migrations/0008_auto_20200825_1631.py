# Generated by Django 3.1 on 2020-08-25 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0007_order_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='user_id',
        ),
    ]