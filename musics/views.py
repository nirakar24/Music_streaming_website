from django.shortcuts import  render
from .models import Music

def homePage(request):
    music=Music.objects.all()
    music_list=list(Music.objects.all().values())
    return render(request,'home.html',{
        'music':music,
        'music_list':music_list
    })