# Generated by Django 3.0.9 on 2021-08-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20210820_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas_postulada',
            name='areas_de_interes',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='cargo_1',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='cargo_10',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='cargo_2',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='cargo_3',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='cargo_4',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='cargo_5',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='cargo_6',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='cargo_7',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='cargo_8',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='cargo_9',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='empresa_10',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='formacion_2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='otras_areas_de_interes',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personas_postulada',
            name='referido_por',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
