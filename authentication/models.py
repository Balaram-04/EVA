from django.db import models
#from django.contrib.auth.models import user

# Create your models here.
class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'
    def  __str__(self):
        return  self.email+":"+self.first_name+":"+self.last_name