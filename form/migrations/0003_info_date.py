# Generated by Django 4.0.5 on 2022-06-20 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_rename_father_name_info_father_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
