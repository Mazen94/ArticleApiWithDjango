from django.db import models



class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    tags = models.TextField()
    image = models.ImageField(blank=False, null=False)
   
def __str__(self):
    return "{} - {} - {} - {}".format(self.title, self.description, self.tags,self.image)
    
 