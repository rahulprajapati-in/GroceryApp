# Generated by Django 3.1 on 2020-08-25 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0010_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(default=1, upload_to='groceryapp/static/img/'),
        ),
    ]