from django.db import models

class data(models.Model):
    title = models.CharField(max_length=100,null=True)
    desc = models.TextField(max_length=200,null=True)
    name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    country = models.CharField(max_length=100,null=True)
    town = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100,null=True)
    phone_number = models.CharField(max_length=100,null=True)
    img = models.ImageField(upload_to="media/person_image",null=True)
    logo=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.title
class ability(models.Model):
    title = models.CharField(max_length=100,null=True)
    desc = models.TextField(max_length=200,null=True)
    icon = models.CharField(max_length=200, null=True)
    path1 = models.CharField(max_length=2000,null=True)
    path2 = models.CharField(max_length=2000,null=True)
    def __str__(self):
        return self.title
class tahsil(models.Model):
    title = models.CharField(max_length=100,null=True)
    desc = models.CharField(max_length=100, null=True)
    date = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.title
class tajrobeh(models.Model):
    title = models.CharField(max_length=100,null=True)
    desc = models.CharField(max_length=100, null=True)
    date = models.CharField(max_length=100, null=True)
class work_place(models.Model):
    title_work_place = models.CharField(max_length=150,null=True)
    email= models.EmailField(max_length=150,null=True)
    phone_number = models.CharField(max_length=100, null=True)
class my_work_img(models.Model):
    img=models.ImageField(upload_to="media/person_image",null=True)

