# Generated by Django 4.2 on 2023-09-08 05:40

import ckeditor_uploader.fields
import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_course_product_thumbnail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='links_to_ads',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='A link that will take to ads', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='links_to_others_stores',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='A link that will take to the store', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='links_to_others_suppliers',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='product_thumbnail',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dvc5exd3c/image/upload/v1694151185/Image-Coming-Soon_lwf1t8.png', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='course',
            name='store_logo',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dvc5exd3c/image/upload/v1694151185/Image-Coming-Soon_lwf1t8.png', max_length=255, verbose_name='image'),
        ),
    ]