# Generated by Django 3.2.14 on 2022-08-03 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='persona',
            unique_together={('pais', 'apelativo')},
        ),
        migrations.AddConstraint(
            model_name='persona',
            constraint=models.CheckConstraint(check=models.Q(('edad__gte', 18)), name='edad_mayor_18'),
        ),
    ]
