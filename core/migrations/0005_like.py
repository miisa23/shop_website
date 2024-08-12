# Generated by Django 5.0.7 on 2024-08-10 10:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='core.product')),
                ('user', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
