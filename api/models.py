from django.db import models

# Create your models here.
class user(models.Model):
    email_id=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    name=models.CharField(max_length=30)
    mobile_number=models.CharField(max_length=15)
    city=models.CharField(max_length=30)

class reset(models.Model):
    user_id=models.IntegerField()
    OTP=models.IntegerField()

class activations(models.Model):
    user_id=models.IntegerField()
    activation=models.CharField(max_length=10)


class AddHouse(models.Model):
    owner_name=models.CharField(max_length=50)
    owner_contect_number=models.CharField(max_length=15)
    house_type=models.IntegerField()
    rent=models.CharField(max_length=20)
    house_facing=models.CharField(max_length=30)
    area=models.CharField(max_length=30)
    conditions=models.CharField(max_length=200)
    Facilities=models.CharField(max_length=200)
    city=models.CharField(max_length=30)
    picture1=models.FileField(upload_to='HousePictures')
    picture2 = models.FileField(upload_to='HousePictures')
    picture3 = models.FileField(upload_to='HousePictures')


class varify_mail(models.Model):
    user_id=models.IntegerField()
    verify_otp=models.CharField(max_length=20)