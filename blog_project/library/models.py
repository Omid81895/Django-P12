from django.db import models

# Create your models here.
class Book(models.Model):
    READING = [
        ('D', "Done"),
        ('SR' , "Still Reading"),
        ('NR' , "Not Read")
    ]
    title = models.CharField()
    author = models.CharField()
    read_status = models.CharField(
        max_length= 2,
        choices= READING, default='NR')
    added_date = models.DateTimeField(auto_now= True)
    note = models.TextField()
    
    RANKING = [
        (1 , 'High') ,
        (2 ,'Medium' ) ,
        (3 , 'Low') ,
    ]
    priority = models.IntegerField(
        choices= RANKING,default=3
    )
    def __str__(self):
        return self.title