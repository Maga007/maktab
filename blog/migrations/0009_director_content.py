# Generated by Django 4.1.7 on 2023-03-22 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_name_director_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='content',
            field=models.TextField(null=True, verbose_name='Director haqida'),
        ),
    ]
