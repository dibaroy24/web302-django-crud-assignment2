from django import forms
from .models import Movie, Poster

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'wwesuperstars')

# The ThemeSongForm form classes should include an exclude variable which is
# a tuple of form fields to exclude from being required by the form

class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        exclude = ('movie',)
        fields = ('role', 'image')
        # fields = ('image',)
