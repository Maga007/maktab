# Generated by Django 4.1.5 on 2023-03-10 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_info_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='phone',
            field=models.IntegerField(default='+998 (99) 999-99-99', verbose_name='Tel raqami'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.IntegerField(default='+998 99 999-99-99', verbose_name='Tel raqami'),
        ),
    ]