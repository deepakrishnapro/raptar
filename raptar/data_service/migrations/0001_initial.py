# Generated by Django 3.1.1 on 2020-10-14 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productid', models.AutoField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=250)),
                ('productversion', models.CharField(max_length=10)),
            ],
        ),
    ]
