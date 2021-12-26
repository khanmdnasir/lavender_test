from django.db import models


class Mobile(models.Model):
    brand_name=models.CharField(max_length=255)
    model=models.CharField(max_length=255)
    color=models.CharField(max_length=255)
    jan_code=models.IntegerField(unique=True)
    image=models.ImageField(upload_to="mobile_images",blank=True,null=True)