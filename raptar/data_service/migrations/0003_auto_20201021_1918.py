# Generated by Django 3.1.1 on 2020-10-21 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_service', '0002_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='productid',
            new_name='product',
        ),
    ]
