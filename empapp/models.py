from django.db import models

class Emp(models.Model):

    ename=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    def __str__(self):
        return self.ename


