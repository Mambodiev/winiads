# Generated by Django 4.2 on 2023-12-15 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_course_facebook_care_alter_course_button'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aliexpressordergrowth',
            options={'verbose_name_plural': 'Aliexpress Order Growth'},
        ),
        migrations.AlterModelOptions(
            name='otheraliexpresssupplierslinks',
            options={'verbose_name_plural': 'Other Aliexpress Suppliers Links'},
        ),
        migrations.AlterModelOptions(
            name='othershopifylinks',
            options={'verbose_name_plural': 'Other Shopify Links'},
        ),
        migrations.AlterModelOptions(
            name='pricing',
            options={'verbose_name_plural': 'Pricings'},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'verbose_name_plural': 'Stores'},
        ),
    ]
