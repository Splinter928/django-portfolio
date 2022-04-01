from django.db import models
import datetime


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
#    image = models.ImageField(upload_to='blog/images/')
#    url = models.URLField(blank=True)   #We used 'blank=True' to open url in new tab
    date = models.DateField()

    def __str__(self): #return title in admin-panel
        return self.title