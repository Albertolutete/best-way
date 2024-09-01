# Generated by Django 5.0.2 on 2024-08-29 21:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0002_categoria_tipo'),
        ('employees', '0010_remove_employee_categoria_laboral_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='funcao_chefia_nova',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='corecode.categorianova', verbose_name='funcao de chefia nova'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='funcao_chefia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='corecode.funcaochefia', verbose_name='funcao de chefia antiga'),
        ),
    ]
