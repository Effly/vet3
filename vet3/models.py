# vet3/models.py

from django.db import models

class Appointment(models.Model):
    OWNER_NAME_MAX_LENGTH = 100
    PET_NAME_MAX_LENGTH = 100
    PET_TYPE_CHOICES = [
        ('dog', 'Собака'),
        ('cat', 'Кошка'),
        ('other', 'Другое'),
    ]
    SERVICE_CHOICES = [
        ('general', 'Осмотр'),
        ('vaccination', 'Вакцинация'),
        ('surgery', 'Операция'),
    ]

    owner_name = models.CharField(max_length=OWNER_NAME_MAX_LENGTH)
    pet_name = models.CharField(max_length=PET_NAME_MAX_LENGTH)
    pet_type = models.CharField(max_length=10, choices=PET_TYPE_CHOICES)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        unique_together = ('date', 'time')

    def __str__(self):
        return f"{self.owner_name} - {self.pet_name} ({self.pet_type})"
