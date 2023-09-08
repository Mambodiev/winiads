# Generated by Django 4.2 on 2023-09-08 01:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_course_product_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='product_thumbnail',
            field=cloudinary.models.CloudinaryField(default='thumbnails/default_store_logo.jpg', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='course',
            name='store_logo',
            field=cloudinary.models.CloudinaryField(default='image_store/default_store_logo.jpg', max_length=255, verbose_name='image'),
        ),
    ]
