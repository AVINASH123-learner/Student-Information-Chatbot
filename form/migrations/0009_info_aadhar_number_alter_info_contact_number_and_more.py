# Generated by Django 4.0.5 on 2022-06-20 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_info_contact_number_info_father_contact_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='Aadhar_Number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='Contact_Number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='Father_Contact_Number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='Mother_Contact_Number',
            field=models.IntegerField(null=True),
        ),
    ]