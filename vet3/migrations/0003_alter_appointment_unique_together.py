# Generated by Django 4.2.16 on 2024-12-24 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vet3', '0002_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('date', 'time')},
        ),
    ]