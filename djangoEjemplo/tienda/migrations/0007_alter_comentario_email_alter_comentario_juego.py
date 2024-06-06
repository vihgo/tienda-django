# Generated by Django 5.0.1 on 2024-06-06 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='juego',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='tienda.juego'),
        ),
    ]
