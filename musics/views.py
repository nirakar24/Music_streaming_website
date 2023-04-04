from django.shortcuts import  render

def homePage(request):
    # musics=list(Music.objects.all().values())
    return render(request,'home.html')