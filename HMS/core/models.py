from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import date, datetime

User = get_user_model()


# Create your models here.
class PatientProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    height = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)
    g = (('M', 'Male'), ('F', 'Female'))
    bg = (('OP', 'O +ve'), ('ON', 'O -ve'), ('AP', 'A +ve'), ('AN', 'A -ve'),
          ('BP', 'B +ve'), ('BN', 'B -ve'), ('ABP', 'AB +ve'), ('ABN', 'AB -ve'))
    gender = models.CharField(max_length=6, choices=g, default='M')
    bloodgroup = models.CharField(max_length=6, choices=bg, default='OP')
    birthdate = models.DateField(default='16/04/2003')
    phone_number = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class DoctorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone_number = models.IntegerField(default=0)
    birthdate = models.DateField()
    g = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=6, choices=g, default='M')
    # bg = (('OP', 'O +ve'), ('ON', 'O -ve'), ('AP', 'A +ve'), ('AN', 'A -ve'),
    #       ('BP', 'B +ve'), ('BN', 'B -ve'), ('ABP', 'AB +ve'), ('ABN', 'AB -ve'))
    # bloodgroup = models.CharField(max_length=6, choices=bg, default='OP')
    speciality = models.TextField(default='MBBS')
    work_address = models.TextField(default='none')
    certificate = models.FileField(upload_to='certi/', default='w.pdf')


    def __str__(self):
        return self.user.username
