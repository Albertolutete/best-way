# Generated by Django 5.0.2 on 2024-08-29 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_estabelecimento_remove_employee_estabelecimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='nacionalidade',
            field=models.CharField(default='NaN', max_length=50),
        ),
    ]
