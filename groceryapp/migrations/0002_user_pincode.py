# Generated by Django 3.0.6 on 2020-05-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pincode',
            field=models.CharField(default=1, max_length=6),
        ),
    ]