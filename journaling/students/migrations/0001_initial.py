# Generated by Django 4.2.1 on 2023-05-17 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Ad')),
                ('surname', models.CharField(max_length=250, verbose_name='Soyad')),
                ('patronymic', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Ata adı')),
                ('gender', models.CharField(choices=[('male', 'Kişi'), ('female', 'Qadın')], max_length=10, null=True, verbose_name='Cinsi')),
            ],
            options={
                'verbose_name_plural': 'Tələbələr',
            },
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Qrupun adı')),
                ('starosta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student', verbose_name='Tələbə')),
            ],
            options={
                'verbose_name_plural': 'Qruplar',
            },
        ),
    ]