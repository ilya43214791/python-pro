# Generated by Django 4.2.3 on 2023-07-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_itemsdecor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsdecor',
            name='active',
            field=models.FloatField(default=False, help_text='Показувати або не показувати товар', verbose_name='Active'),
        ),
    ]
