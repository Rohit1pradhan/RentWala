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
    current_city=models.CharField(max_length=30)

class addhouse(models.Model):
    owner_id=models.IntegerField()
    house_type=models.CharField(max_length=100)
    rent=models.CharField(max_length=20)
    facing=models.CharField(max_length=30)
    area=models.CharField(max_length=30)
    conditions=models.CharField(max_length=200)
    facillities=models.CharField(max_length=200)
    city=models.CharField(max_length=30)


class varify_mail(models.Model):
    user_id=models.IntegerField()
    verify_otp=models.CharField(max_length=20)