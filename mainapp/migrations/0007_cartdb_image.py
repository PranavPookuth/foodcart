# Generated by Django 3.2.10 on 2023-06-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20230616_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]