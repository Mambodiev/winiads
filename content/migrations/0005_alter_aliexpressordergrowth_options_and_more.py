# Generated by Django 4.2 on 2023-09-17 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_alter_store_options_course_product_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aliexpressordergrowth',
            options={'verbose_name_plural': '5. AliexpressOrderGrowth'},
        ),
        migrations.AlterModelOptions(
            name='otheraliexpresssupplierslinks',
            options={'verbose_name_plural': '7 Other Aliexpress Suppliers Links'},
        ),
        migrations.AlterModelOptions(
            name='othershopifylinks',
            options={'verbose_name_plural': '3 Other Shopify Links'},
        ),
        migrations.AlterModelOptions(
            name='pricing',
            options={'verbose_name_plural': '6 Pricings'},
        ),
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name_plural': '3 Subscriptions'},
        ),
        migrations.AddField(
            model_name='otheraliexpresssupplierslinks',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='otheraliexpresssupplierslinks',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Aliexpress price', max_digits=10),
        ),
        migrations.AddField(
            model_name='othershopifylinks',
            name='countries',
            field=models.CharField(blank=True, choices=[('United States', 'United States'), ('United Kingdom', 'United Kingdom'), ('Canada', 'Canada'), ('Australia', 'Australia'), ('New Zealand', 'New Zealand'), ('Sweden', 'Sweden'), ('Denmark', 'Denmark'), ('Iceland', 'Iceland'), ('Norway', 'Norway'), ('Finland', 'Finland'), ('The Netherlands', 'The Netherlands'), ('Ireland', 'Ireland'), ('Germany', 'Germany'), ('South Korea', 'South Korea'), ('Switzerland', 'Switzerland'), ('Belgium', 'Belgium'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('France', 'France'), ('Spain', 'Spain'), ('Portugal', 'Portugal'), ('Austria', 'Austria'), ('Hungary', 'Hungary'), ('Poland', 'Poland'), ('Czech Republic', 'Czech Republic'), ('UAE', 'UAE'), ('South Africa', 'South Africa'), ('The Philippines', 'The Philippines'), ('Japan', 'Japan'), ('Singapore', 'Singapore'), ('Argentina', 'Argentina'), ('Mexico', 'Mexico')], default='United States', max_length=250, null=True),
        ),
    ]
