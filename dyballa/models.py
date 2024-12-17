from django.db import models

# Create your models here.
class  Argentina(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    height=models.IntegerField()
    weight=models.IntegerField()
    debut_date=models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return f"{self.name} {self.age}{self.height}"

