from django.db import models

# Create your models here.


class Login (models.Model):
    login_id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200) 

class User (models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    place = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    points = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='static/user')

class Prayer(models.Model):
    prayer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    point = models.CharField(max_length=200)

class Prayer_marking(models.Model):
    prayer_mark_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    prayer =models.ForeignKey(Prayer,on_delete=models.CASCADE)
    date= models.CharField(max_length=200)
    ontime = models.CharField(max_length=200)
    aftertime = models.CharField(max_length=200)
    with_imam = models.CharField(max_length=200)
    missed = models.CharField(max_length=200)


