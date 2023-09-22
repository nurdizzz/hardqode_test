from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Video(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='images', null=True)
    video = models.FileField(upload_to='video', null= True,
                             validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.headline}'

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    videos = models.ManyToManyField(Video)

    def __str__(self):
        return f'{self.name}'