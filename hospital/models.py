from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    special=models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    mobile=models.IntegerField(null=True)
    age=models.IntegerField(null=True)
    address=models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()

    def __str__(self):
        return self.Doctor.name+"__"+self.Patient.name


