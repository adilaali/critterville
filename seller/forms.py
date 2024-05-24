from django import forms
from .models import PetDetails

class PetDetailsForm(forms.ModelForm):
    class Meta():
        model=PetDetails
        fields='__all__'

class UpdateSellerForm(forms.ModelForm):
    class Meta():
        model=PetDetails
        fields='__all__'

