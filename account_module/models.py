from django.db import models

# Create your models here.

class register_model(models.Model):
    username=models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100, null=True)
    desc = models.CharField(max_length=350,null=True)
    date = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.username