from django.db import models

OCCUPANCY_OPTIONS = {
    '1': 'single-sharing',
    '2': 'double-sharing',
    '3': 'triple-sharing',
    '4': 'quad-sharing',
}
GENDER_TYPE = {
    '1': 'male',
    '2': 'Female',
    '3': 'Other',
}


class Provider(models.Model):
    objects = None
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    mail = models.EmailField()
    age = models.IntegerField()
    city = models.CharField(max_length=25)
    mobile = models.CharField(max_length=20)
    req_occupancy = models.CharField(max_length=10, choices=OCCUPANCY_OPTIONS.items())
    gender = models.CharField(max_length=8, choices=GENDER_TYPE.items())

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Renter(models.Model):
    objects = None
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    mail = models.EmailField()
    age = models.IntegerField()
    city = models.CharField(max_length=25)
    mobile = models.CharField(max_length=20)
    req_occupancy = models.CharField(max_length=10, choices=OCCUPANCY_OPTIONS.items())
    gender = models.CharField(max_length=8, choices=GENDER_TYPE.items())

    def __str__(self):
        return f"{self.fname} {self.lname}"
