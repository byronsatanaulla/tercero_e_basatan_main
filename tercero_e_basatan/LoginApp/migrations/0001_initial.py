
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=256)),
                ('correo', models.CharField(max_length=256, unique=True)),
                ('usuario', models.CharField(max_length=100, unique=True)),
                ('contrasena', models.CharField(max_length=150)),
                ('ciudad', models.ForeignKey(default=False, on_delete=django.db.models.deletion.PROTECT, to='LoginApp.ciudades')),
                ('genero', models.ForeignKey(default=False, on_delete=django.db.models.deletion.PROTECT, to='LoginApp.generos')),
            ],
        ),
    ]
