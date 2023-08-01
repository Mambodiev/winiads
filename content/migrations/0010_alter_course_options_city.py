# Generated by Django 4.2 on 2023-07-31 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_rename_name_course_name_of_product_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-id']},
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('population', models.PositiveIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='content.course')),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
    ]
