from django.views.generic import ListView, DetailView
from .models import Anime

class AnimeListView(ListView):
    model = Anime
    template_name = 'anime_list.html'  # подразумевает: <app_name>/anime_list.html
    context_object_name = 'animes'     # имя переменной контекста в шаблоне

class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'anime_detail.html' # подразумевает: <app_name>/anime_detail.html
    context_object_name = 'anime'       # имя переменной контекста в шаблоне
