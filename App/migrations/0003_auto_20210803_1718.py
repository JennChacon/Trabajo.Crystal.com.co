# Generated by Django 3.0.9 on 2021-08-03 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20210803_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas_postulada',
            name='apellidos',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='comentarios',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='empresa_1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='empresa_10',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='empresa_2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='empresa_3',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='empresa_4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='empresa_5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='empresa_6',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='empresa_7',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='empresa_8',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='empresa_9',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='funciones_y_logros_1',
            field=models.TextField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='funciones_y_logros_10',
            field=models.TextField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='funciones_y_logros_2',
            field=models.TextField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='funciones_y_logros_3',
            field=models.TextField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='funciones_y_logros_4',
            field=models.TextField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='funciones_y_logros_5',
            field=models.TextField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='funciones_y_logros_6',
            field=models.TextField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='funciones_y_logros_7',
            field=models.TextField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='funciones_y_logros_8',
            field=models.TextField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='funciones_y_logros_9',
            field=models.TextField(max_length=20000, null=True),
        ),
    ]
