from django.forms import ModelForm
from .models import Squirrel

from .models import Squirrel

class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = ['Longitude',
                  'Latitude',
                  'Unique_Squirrel_ID',
                  'Shift',
                  'Date',
                  'Age',
        ]

class AddForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'

class DetailsForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'


