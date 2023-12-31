# Generated by Django 4.2 on 2023-12-31 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_rename_store_mainshopifystore_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otheraliexpresssupplierslinks',
            name='link',
            field=models.TextField(blank=True, help_text='A link that will take to a single the Other Aliexpress Suppliers Links', null=True),
        ),
        migrations.AlterField(
            model_name='othershopifylinks',
            name='link',
            field=models.TextField(blank=True, help_text='A link that will take to a single the Other Shopify Links', null=True),
        ),
    ]
