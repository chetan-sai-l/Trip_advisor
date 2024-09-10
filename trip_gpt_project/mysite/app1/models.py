from django.db import models

class TravelPreference(models.Model):
    group_type = models.CharField(max_length=100,default='None')
    transportation = models.CharField(max_length=100,default='None')
    accommodation = models.CharField(max_length=100,default='None')
    outdoor_adventures = models.CharField(max_length=100,default='None')
    cultural_experiences = models.CharField(max_length=100,default='None')
    specific_cuisine = models.CharField(max_length=100,default='None')
    num_days = models.CharField(max_length=100,default='None')
    # number_days = models.CharField(max_length=100,default='None')
    plan = models.CharField(max_length=2000,default='None')
    question = models.CharField(max_length=2000,default='None')
    def __str__(self):
        return f"{self.group_type}"

# class InterestsAndActivities(models.Model):
    

#     def __str__(self):
#         return f"{self.outdoor_adventures}, {self.cultural_experiences}, {self.specific_cuisine}"
