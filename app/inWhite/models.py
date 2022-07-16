import datetime

from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_init

class Property(models.Model):
    name = models.CharField(max_length=46, unique=True)
    area = models.IntegerField()
    address = models.CharField(blank=True, max_length=200)
    description = models.CharField(blank=True, max_length=400)
    registration_date = models.DateTimeField()
   # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, upload_to="media/")

    PROPERTY_TYPE_CHOICES = [
        ('NNN', '-----'),
        ('APT', 'Apartments'),
        ('HTL', 'Hotel'),
        ('HSE', 'House'),
    ]

    property_type = models.CharField(max_length=3, choices=PROPERTY_TYPE_CHOICES, default='NNN')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "properties"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.registration_date = datetime.datetime.now()

    def get_photo(self):
        return self.photo.url




# Create your models here.
