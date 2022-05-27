# Generated by Django 4.0.4 on 2022-05-02 11:47

from django.db import migrations, models
import sheets.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(default=sheets.models.current_year, verbose_name='year')),
                ('month', models.PositiveIntegerField(default=sheets.models.current_month, verbose_name='month')),
                ('data', models.JSONField(default=dict)),
            ],
        ),
    ]