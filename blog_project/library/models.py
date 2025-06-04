from django.db import models

# Create your models here.
class Book(models.Model):
    READING = (
        ('' , "How much did you read this book?"),
        ('D', "Done"),
        ('SR' , "Still Reading"),
        ('NR' , "Not Read")
        )
    title = models.CharField()
    author = models.CharField()
    read_status = models.CharField(
        max_length= 2,
        choices= READING)
    added_date = models.DateTimeField(auto_now= True)
    note = models.TextField()
    
    RANKING = (
        ('', 'Pick your priority'),
        (1 , 'High') ,
        (2 ,'MEDIUM' ) ,
        (3 , 'LOW') ,
        )
    priority = models.IntegerField(
        choices= RANKING,
        default= 3
    )