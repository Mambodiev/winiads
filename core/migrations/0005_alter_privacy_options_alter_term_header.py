# Generated by Django 4.2 on 2024-01-26 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_privacy_term'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='privacy',
            options={'verbose_name_plural': 'Privacies'},
        ),
        migrations.AlterField(
            model_name='term',
            name='header',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
