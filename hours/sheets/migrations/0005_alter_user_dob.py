# Generated by Django 4.0.4 on 2023-02-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0004_user_sheba_number_user_account_number_user_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='date_of_birth'),
        ),
    ]
