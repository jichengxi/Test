from django.db import models

# Create your models here.

class BookInfo(models.Model):
    """图书模型表"""
    bittle = models.CharField(max_length=20)
    bpub_date = models.DateField()

    def __str__(self):
        return self.bittle
