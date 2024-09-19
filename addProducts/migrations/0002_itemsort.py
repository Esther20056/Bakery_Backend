# Generated by Django 5.0.4 on 2024-09-12 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addProducts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='sorts')),
                ('category', models.CharField(max_length=255)),
                ('current_price', models.CharField(default='NGN', max_length=20)),
                ('size', models.CharField(blank=True, max_length=20, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=255)),
                ('flavour', models.CharField(max_length=200)),
                ('layers_display', models.TextField()),
            ],
        ),
    ]
