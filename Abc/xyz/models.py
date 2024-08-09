from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    roll=models.DecimalField(max_digits=3,decimal_places=0)
    department=models.CharField(max_length=60)
    notes=models.TextField()

    def __str__(self):
        return f"Name-{self.name} Roll-{self.roll}"