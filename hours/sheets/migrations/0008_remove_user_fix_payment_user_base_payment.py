# Generated by Django 4.0.4 on 2023-04-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0007_sheet_user_name_user_comment_alter_sheet_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='fix_payment',
        ),
        migrations.AddField(
            model_name='user',
            name='base_payment',
            field=models.IntegerField(default=0, verbose_name='base_payment'),
        ),
    ]
