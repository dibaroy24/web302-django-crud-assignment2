# Import the ListView class which is designed to list all of the items
# in the database and DetailView class which selects one item from the database
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# import the reverse_lazy() function which will redirect to a page but only
# after a data process has completed
from django.urls import reverse_lazy

# Lastly, import the WWESuperstarForm class from the forms module
# and the WWESuperstar model form models module
from .forms import WWESuperstarForm
from .models import WWESuperstar

# Create your views here.
class WWESuperstarList(ListView):
    # Set the model variable to the Musician class to specify which mdoel
    # we want to list in this view
    model = WWESuperstar
    # Set the template_name to the name of the corresponding Django template
    # which you want displayed
    template_name = 'index.html.django'
    # Finally set the context_object_name variable to the name of the
    # variable you want to use to access and loop through the list of data
    context_object_name = 'wwesuperstars'

class WWESuperstarDetail(DetailView):
    model = WWESuperstar
    template_name = 'detail.html.django'
    context_object_name = 'wwesuperstar'

class WWESuperstarCreate(CreateView):
    model = WWESuperstar
    template_name = 'add.html.django'
    # Set the fields variable to WWESuperstarForm.Meta.fields to specify that
    # you want all form fields associated with this form to be included
    # in the creation of this data
    fields = WWESuperstarForm.Meta.fields
    # Finally set the success_url variable to the reverse_lazy function to
    # indicate what template the user should be redirected to once the
    # has been processed
    success_url = reverse_lazy('home')

class WWESuperstarUpdate(UpdateView):
    model = WWESuperstar
    template_name = 'edit.html.django'
    fields = WWESuperstarForm.Meta.fields
    success_url = reverse_lazy('home')

class WWESuperstarDelete(DeleteView):
    model = WWESuperstar
    template_name = 'delete.html.django'
    success_url = reverse_lazy('home')
