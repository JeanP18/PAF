# Generated by Django 4.2.7 on 2023-11-20 20:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nro_documento', models.CharField(max_length=11)),
                ('razon_social', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='GruposProveedor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codigo_grupo', models.CharField(max_length=15)),
                ('grupo_descripcion', models.CharField(max_length=100)),
                ('activo', models.BooleanField()),
                ('responsable_grupo', models.CharField(max_length=25)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finals.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='LineasArticulos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codigo_linea', models.CharField(max_length=15)),
                ('linea_descripcion', models.CharField(max_length=100)),
                ('activo', models.BooleanField()),
                ('responsable_linea', models.CharField(max_length=25)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finals.gruposproveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codigo_marca', models.CharField(max_length=14)),
                ('marca_nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadesMedida',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('unidad_nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('username', models.CharField(max_length=25)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre_comercial', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finals.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='SublineasArticulos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codigo_sublinea', models.CharField(max_length=15)),
                ('sublinea_descripcion', models.CharField(max_length=100)),
                ('estado', models.BooleanField()),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finals.lineasarticulos')),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codigo_sku', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=150)),
                ('factor_compra', models.IntegerField()),
                ('factor_reparto', models.IntegerField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finals.empresa')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finals.gruposproveedor')),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finals.lineasarticulos')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finals.marcas')),
                ('sublinea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finals.sublineasarticulos')),
                ('unidad_medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finals.unidadesmedida')),
            ],
        ),
    ]