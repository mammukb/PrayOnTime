# Generated by Django 3.2.24 on 2024-05-23 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prayapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(),
        ),
    ]
