# Generated by Django 5.1.1 on 2025-02-05 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='imege',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.URLField(blank=True, null=True),
        ),
    ]
