# Generated by Django 4.2.7 on 2023-12-14 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chave',
            name='status',
            field=models.CharField(max_length=150),
        ),
    ]
