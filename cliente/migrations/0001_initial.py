# Generated by Django 4.1.5 on 2023-01-20 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, verbose_name='tipo')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'db_table': 'estado',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Pueblo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Pueblo')),
            ],
            options={
                'verbose_name': 'Pueblo',
                'verbose_name_plural': 'Pueblos',
                'db_table': 'pueblo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, unique=True, verbose_name='Ip del Cliente')),
                ('cedula', models.CharField(max_length=12, unique=True, verbose_name='Cedula del Cliente')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Cliente')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido del Cliente')),
                ('telefono_uno', models.CharField(max_length=12, verbose_name='Primer Telefono ')),
                ('telefonos_dos', models.CharField(blank=True, max_length=12, null=True, verbose_name='Segundo Telefono')),
                ('mensualidad', models.PositiveIntegerField(blank=True, null=True, verbose_name='Mensualidad')),
                ('fecha_instalacion', models.DateField(blank=True, null=True, verbose_name='Fecha de Instalacion')),
                ('direccion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Direccion')),
                ('vereda', models.CharField(blank=True, max_length=100, null=True, verbose_name='Vereda')),
                ('tipo_instalacion', models.CharField(blank=True, choices=[('Fibra Optica', 'Fibra'), ('Radio Enlace', 'Radio')], max_length=20, null=True, verbose_name='Tipo de Instalacion')),
                ('status', models.CharField(blank=True, choices=[('arriba', 'Activo'), ('abajo', 'Sin servicio')], max_length=20, null=True, verbose_name='Estado')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('id_Estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Estado', to='cliente.estado')),
                ('id_Pueblo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pueblo', to='cliente.pueblo')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'cliente',
                'ordering': ['ip'],
            },
        ),
    ]
