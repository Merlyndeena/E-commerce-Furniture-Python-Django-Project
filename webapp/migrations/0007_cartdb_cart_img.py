# Generated by Django 4.0.3 on 2024-11-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_alter_orderdb_totalp'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='cart_img',
            field=models.ImageField(blank=True, null=True, upload_to='Cart Images'),
        ),
    ]