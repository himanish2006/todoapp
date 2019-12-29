# Create your models here.
from django.db import models


class ToDo(models.Model):
    sr_no =models.AutoField(primary_key=True)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,blank =True)

    def __str__(self):
        return self.content







