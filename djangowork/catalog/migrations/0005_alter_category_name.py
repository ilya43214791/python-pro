# Generated by Django 4.2.3 on 2023-07-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_good_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='gdgd'),
        ),
    ]
