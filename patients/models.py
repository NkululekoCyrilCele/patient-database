from django.db import models


class Patient(models.Model):
    patient_id = models.PositiveIntegerField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    medical_diagnosis = models.CharField(max_length=50)
    urine_ph = models.FloatField()

    def __str__(self):
        return f'Patient: {self.first_name} {self.last_name}'
