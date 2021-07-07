# Generated by Django 3.2.5 on 2021-07-07 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f_contacto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formulario_contacto',
            options={'verbose_name': 'Proveedor', 'verbose_name_plural': 'Proveedores'},
        ),
        migrations.RemoveField(
            model_name='formulario_contacto',
            name='company',
        ),
        migrations.RemoveField(
            model_name='formulario_contacto',
            name='message',
        ),
        migrations.RemoveField(
            model_name='formulario_contacto',
            name='subject',
        ),
        migrations.AddField(
            model_name='formulario_contacto',
            name='direccion',
            field=models.TextField(null=True, verbose_name='direccion'),
        ),
    ]
