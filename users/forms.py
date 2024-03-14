from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"form-control"}))

class RegisterForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def clean_username(self):
        username = self.cleaned_data.get('username', None)
        if len(username) < 4:
            raise forms.ValidationError("Username must be at least 4 characters long.")
        elif len(username) > 20:
            raise forms.ValidationError("Username must be at most 20 characters long.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')
        elif password and len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return cleaned_data

class ProfileForm(forms.ModelForm):
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number', None)
        if phone_number and (not phone_number.startswith('+998') or len(phone_number) != 13):
            raise forms.ValidationError("Phone number should be in correct format (+998XXXXXXXXX).")
        return phone_number

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'bio', 'phone_number', 'photo', 'email')
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'bio': forms.TextInput(attrs={"class": "form-control"}),
            'photo': forms.FileInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
        }
    


    