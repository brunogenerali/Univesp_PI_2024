# Generated by Django 5.0.4 on 2024-09-24 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faltas', '0005_dadosexcel_mensagem_falta'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DadosExcel',
        ),
        migrations.AddField(
            model_name='menssagem',
            name='falta_data',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]