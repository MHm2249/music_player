from django.shortcuts import render
from .models import Song

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'player/song_list.html', {'songs': songs})


def home(request):
    return render(request, 'player/home.html')
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'