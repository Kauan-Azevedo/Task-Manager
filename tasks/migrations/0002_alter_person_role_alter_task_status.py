# Generated by Django 4.2.7 on 2023-11-24 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.IntegerField(choices=[(0, 'Cliente'), (1, 'Colaborador')], default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pendente'), (1, 'Concluida')], default=0),
        ),
    ]
