from django.db import models
class web1(models.Model):
    Name=models.CharField(max_length=20)
    Number=models.IntegerField(20)

def _str_ (self):
    return self.Name()


# Create your models here.
