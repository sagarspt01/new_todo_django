from django.db import models

# Create your models here.
class Todo(models.Model): # models=single definative source of information about your database
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=200)
    isDone=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        # return self.title[:20] # for 20 character only
        return self.title
