from django.urls import path
from .views import AnimeListView, AnimeDetailView

urlpatterns = [
    path('', AnimeListView.as_view(), name='anime_list'),
    path('anime/<int:pk>', AnimeDetailView.as_view(), name='anime_detail'),  # 'pk' это первичный ключ, который Django использует для поиска отдельного объекта
]
