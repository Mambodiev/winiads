# Generated by Django 4.2 on 2024-01-26 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_privacy_options_alter_term_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privacy',
            name='header',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='header_one',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
