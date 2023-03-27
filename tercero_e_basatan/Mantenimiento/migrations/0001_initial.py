
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Juguetes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('modelo', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
                ('precio', models.CharField(max_length=10, unique=True)),
                ('disponibilidad', models.BooleanField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Mantenimiento.marcas')),
            ],
        ),
    ]
