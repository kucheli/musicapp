from django.db import models


# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=2)
    
    def__str__(self):
        return self.first_name.last_name.age
    
    
class Song(models.Model):
    title = models.CharField(max_length=20)
    date_released = models.DateField()
    likes = models.TextField(max_length= 200)
    artist_id = models.CharField(max_length=50)
    
    def__str__(self):
        return self.title
    
    
class Lyric(models.Model):
    content = models.TextField(max_length=700)
    song_id = models.CharField(max_length=50)
  
    def_str_(self):
        return self.content.song_id    
        
        