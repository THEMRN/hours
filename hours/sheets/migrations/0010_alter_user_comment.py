# Generated by Django 4.0.4 on 2023-05-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0009_sheet_addition1_sheet_base_payment_sheet_reduction1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='comment'),
        ),
    ]
