# Generated by Django 3.1.3 on 2020-11-24 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Valor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('variacion', models.FloatField()),
                ('acumulado', models.FloatField()),
                ('maximo', models.FloatField()),
                ('minimo', models.FloatField()),
                ('volumen', models.FloatField()),
                ('capitalizacion', models.FloatField()),
                ('actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Valor',
                'verbose_name_plural': 'Valores',
            },
        ),
    ]
