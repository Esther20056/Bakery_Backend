# Generated by Django 5.0.4 on 2024-09-14 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addProducts', '0003_delete_itemsort'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newbakes',
            name='layers_display',
            field=models.TextField(blank=True, null=True),
        ),
    ]
