from django.db import models
from datetime import datetime
class Posts(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)
    front_banner = models.ImageField(upload_to='blog/images',default="")
    date_posted =  models.DateField(default="")
    def __str__(self):
        return self.title + f"({str(self.sno)})"