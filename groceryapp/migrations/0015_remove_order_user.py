# Generated by Django 3.1 on 2020-08-26 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0014_orderdone_session_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
