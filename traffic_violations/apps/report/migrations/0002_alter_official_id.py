# Generated by Django 4.2.11 on 2024-04-27 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='official',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
