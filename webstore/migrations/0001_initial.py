# Generated by Django 4.2.4 on 2023-08-22 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Brand name')),
                ('slug_name', models.SlugField(max_length=255, unique=True, verbose_name='Slug name')),
                ('description', models.TimeField(max_length=1020, verbose_name='Description')),
                ('picture_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='Picture URL')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category name')),
                ('description', models.TextField(blank=True, default='', max_length=1020, verbose_name='Category description')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Product name')),
                ('slug_name', models.SlugField(max_length=255, unique=True, verbose_name='Slug name')),
                ('type', models.CharField(max_length=255, verbose_name='Type of product')),
                ('data', models.JSONField(blank=True, max_length=255, null=True, verbose_name='Custom data')),
                ('description', models.TimeField(max_length=1020, verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Price')),
                ('stock_quantity', models.IntegerField(default=0, verbose_name='In stock')),
                ('picture_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='Picture URL')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.brand', verbose_name='Product brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.category', verbose_name='Product category')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_value', models.FloatField(default=5.0, verbose_name='Rating value')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Rating text')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.product', verbose_name='Product')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.category'),
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.product', verbose_name='Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]