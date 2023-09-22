from django.contrib import admin
from .models import Video, Author, Lesson

# Register your models here.
admin.site.register(Video)
admin.site.register(Author)
admin.site.register(Lesson)