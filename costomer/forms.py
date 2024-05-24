from django import forms
from . models import SignUp

class UserSignUpForm(forms.ModelForm):
    Pass_word=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)

    class Meta():
        model=SignUp
        fields='__all__'

class UserLoginForm(forms.ModelForm):
    Pass_word=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)
    
    class Meta():
        model=SignUp
        fields=('Email','Pass_word')

class UpdateBuyerForm(forms.ModelForm):
    class Meta():
        model=SignUp
        fields=('FirstName','LastName','Phone_Number','Email')

class BuyerChangePasswordForm(forms.Form):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)