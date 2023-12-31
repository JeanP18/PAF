# Generated by Django 4.2.7 on 2023-11-22 22:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('finals', '0005_remove_venta_categoria_delete_categoria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanalCliente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('canal_cliente_descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nro_documento', models.CharField(max_length=12)),
                ('nombre_razon_social', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('canal_cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finals.canalcliente')),
            ],
        ),
    ]
