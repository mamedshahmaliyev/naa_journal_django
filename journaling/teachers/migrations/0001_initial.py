# Generated by Django 4.2.1 on 2023-05-17 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Ad')),
                ('surname', models.CharField(max_length=250, verbose_name='Soyad')),
                ('patronymic', models.CharField(max_length=250, verbose_name='Ata adı')),
            ],
        ),
    ]
