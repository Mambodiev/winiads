# Generated by Django 4.2 on 2023-12-31 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_alter_otheraliexpresssupplierslinks_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='shopify_links',
            new_name='main_shopify_links',
        ),
    ]