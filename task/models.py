from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    # # uncomment below after running test_model_has_string_representation

    # def __str__(self):
    #     return self.title



class Project(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    status = models.CharField(max_length=200, choices=[('ongoing', 'ON GOING'), ('paused', 'PAUSED'), ('over', 'OVER')], default='ongoing')



    def check_status(self):
        return self.status
    
