# Generated by Django 4.0.4 on 2022-07-14 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='user',
            name='wage',
            field=models.IntegerField(blank=True, null=True, verbose_name='wage'),
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]
