# Import the forms object from the django module and the WWESuperstar class
# from the models module
from django import forms
from .models import WWESuperstar

# Then create the class for the form as a child class of the ModelForm class
# which is in the forms object.
class WWESuperstarForm(forms.ModelForm):
    # Django uses a nested class called Meta for creating forms which
    # controls the information about the outer class.
    class Meta:
        # The first class variable is called model and it is equal to a new
        # instance of a WWESuperstar class.
        model = WWESuperstar
        # Drop down list to get the current status of the WWE Superstar
        # current_status = forms.ChoiceField(label="", initial='', widget=forms.Select(), required=True)
        # The second class variable is called fields and is a tuple
        # of the names of all of the form fields which should be included in
        # this form.
        fields = ('name', 'image', 'age', 'retired')
