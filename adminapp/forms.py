from django import forms
from . models import Login,Category
from costomer.models import SignUp
from seller . models import PetDetails

class AdminLoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)
    class Meta():
        model=Login
        fields='__all__'

class CategoryForm(forms.ModelForm):
    class Meta():
        model=Category
        fields='__all__'

class UpdateCategoryForm(forms.ModelForm):
    class Meta():
        model=Category
        fields='__all__'

class AdminUpdateBuyerForm(forms.ModelForm):
    class Meta():
        model=SignUp
        fields=('FirstName','LastName','Phone_Number','Email')

class AdminUpdatePetForm(forms.ModelForm):
    class Meta():
        model=PetDetails
        fields='__all__'