from django.urls import path
from .views import MovieList, MovieDetail, MovieCreate, MovieUpdate, MovieDelete, PosterCreate

urlpatterns = [
    path('', MovieList.as_view(), name='movie-home'),
    path('<int:pk>', MovieDetail.as_view(), name='movie-detail'),
    path('add', MovieCreate.as_view(), name='add-movie'),
    path('edit/<int:pk>', MovieUpdate.as_view(), name='edit-movie'),
    path('delete/<int:pk>', MovieDelete.as_view(), name='delete-movie'),
    path('poster/add/<int:pk>', PosterCreate.as_view(), name='add-poster'),
]
