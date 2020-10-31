# Generated by Django 3.1.2 on 2020-10-31 18:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID única para el caso de un Alumno.', primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('tema', models.TextField(max_length=5000)),
            ],
            options={
                'ordering': ['titulo'],
            },
        ),
    ]