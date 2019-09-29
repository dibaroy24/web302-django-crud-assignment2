from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import MovieForm, PosterForm
from .models import Movie, Poster

# Create your views here.
class MovieList(ListView):
    model = Movie
    template_name = 'movie-index.html.django'
    context_object_name = 'movies'

class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie-detail.html.django'
    context_object_name = 'movie'

class MovieCreate(CreateView):
    model = Movie
    template_name = 'add-movie.html.django'
    fields = MovieForm.Meta.fields
    success_url = reverse_lazy('movie-home')

class MovieUpdate(UpdateView):
    model = Movie
    template_name = 'edit-movie.html.django'
    fields = MovieForm.Meta.fields
    success_url = reverse_lazy('movie-home')

class MovieDelete(DeleteView):
    model = Movie
    template_name ='delete-movie.html.django'
    success_url = reverse_lazy('movie-home')

class PosterCreate(CreateView):
    model = Poster
    template_name = 'add-poster.html.django'
    fields = PosterForm.Meta.fields
    success_url = reverse_lazy('movie-home')

    def form_valid(self, form):
        form.instance.movie_id = self.kwargs.get('pk')
        return super(PosterCreate, self).form_valid(form)
