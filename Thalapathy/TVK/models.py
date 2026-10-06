from django.db import models
from django.contrib import admin

class customDB(models.Model):
    name = models.CharField(max_length=12)
    Mobile = models.IntegerField()
    Address = models.TextField()
    RC_Number = models.CharField(max_length=10, primary_key=True)
    DL_Number = models.CharField(max_length=15)
    Vehicle_Model = models.CharField(max_length=12)
    Complaints = models.TextField()


class vehicle_DBAdmin(admin.ModelAdmin):
    list_display = ["name", "Mobile", "Address", "RC_Number", "DL_Number", "Vehicle_Model", "Complaints"]