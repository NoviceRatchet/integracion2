# Generated by Django 5.0.4 on 2024-05-11 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='disponible',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigoProducto',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
