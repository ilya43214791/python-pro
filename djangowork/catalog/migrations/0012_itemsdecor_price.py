# Generated by Django 4.2.3 on 2023-07-19 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_itemsdecor_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsdecor',
            name='price',
            field=models.FloatField(default=1, verbose_name='Ціна'),
            preserve_default=False,
        ),
    ]
