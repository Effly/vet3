# Generated by Django 4.2.16 on 2024-11-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vet3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=100)),
                ('pet_name', models.CharField(max_length=100)),
                ('pet_type', models.CharField(choices=[('dog', 'Собака'), ('cat', 'Кошка'), ('other', 'Другое')], max_length=10)),
                ('service', models.CharField(choices=[('general', 'Осмотр'), ('vaccination', 'Вакцинация'), ('surgery', 'Операция')], max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
