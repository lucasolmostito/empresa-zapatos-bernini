# Generated by Django 3.2.5 on 2021-07-07 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_sale', models.DateTimeField()),
                ('total_quantity', models.PositiveIntegerField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Monto total')),
                ('canceled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='Cantidad de un producto')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Precio')),
                ('canceled', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'verbose_name': 'Detalle de pedido',
                'verbose_name_plural': 'Detalles de pedido',
            },
        ),
    ]