# Generated by Django 5.1.2 on 2024-10-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(blank=True, max_length=100, null=True)),
                ('p_name', models.CharField(blank=True, max_length=100, null=True)),
                ('p_quan', models.IntegerField(blank=True, null=True)),
                ('p_mrp', models.CharField(blank=True, max_length=100, null=True)),
                ('p_desc', models.TextField(blank=True, max_length=200, null=True)),
                ('p_coo', models.CharField(blank=True, max_length=200, null=True)),
                ('p_manu', models.CharField(blank=True, max_length=200, null=True)),
                ('p_img1', models.ImageField(blank=True, null=True, upload_to='Items')),
                ('p_img2', models.ImageField(blank=True, null=True, upload_to='Items')),
                ('p_img3', models.ImageField(blank=True, null=True, upload_to='Items')),
            ],
        ),
    ]