# Generated by Django 3.2.10 on 2023-06-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_cartdb_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
