# Generated by Django 3.2.14 on 2022-08-04 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='stok',
            field=models.PositiveIntegerField(default=0),
        ),
    ]