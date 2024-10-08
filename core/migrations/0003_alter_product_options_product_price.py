# Generated by Django 5.0.7 on 2024-07-29 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_category_options_alter_category_title_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.TextField(default=0, max_length=9, verbose_name='Цена товара'),
        ),
    ]
