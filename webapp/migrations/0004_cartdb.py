# Generated by Django 5.1.2 on 2024-11-12 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_rename_signup_signup_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('prod_name', models.CharField(blank=True, max_length=100, null=True)),
                ('quan', models.IntegerField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, max_length=100, null=True)),
                ('tprice', models.IntegerField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]