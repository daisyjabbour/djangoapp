from django import forms

class TestUserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())  # Use a password input widget
