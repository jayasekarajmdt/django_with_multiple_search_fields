from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class skill(models.Model):
    skill_name=models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name




class freelancer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age=models.IntegerField()
    skills=models.ManyToManyField(skill)
    

    def __str__(self):
        return self.first_name +''+self.last_name