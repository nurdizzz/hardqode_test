from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Author, Video, Lesson

# Create your views here.
class GetVideoView(TemplateView):
    template_name = 'video_platform/video_hosting_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['vide'] = Video.objects.all()
        context['lessons'] = Lesson.objects.all()
        return context