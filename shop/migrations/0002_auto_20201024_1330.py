# Generated by Django 3.1.2 on 2020-10-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='origin',
            field=models.URLField(blank=True, null=True),
        ),
    ]
