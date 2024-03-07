from django import forms
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"form-control"}))



class RegisterForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name', None)
        if first_name:
            if not first_name.isalpha():
                raise forms.ValidationError("Ism faqat harflardan iborat bo'lishi kerak")
        return self.cleaned_data


    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    def clean_first_name(self):
        last_name = self.cleaned_data.get('last_name', None)
        if last_name:
            if not last_name.isalpha():
                raise forms.ValidationError("Ism faqat harflardan iborat bo'lishi kerak")
        return last_name
    
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))

    def check_username(self):
        username = self.cleaned_data.get('username', None)
        if username:
            if len(username)<4:
                raise forms.ValidationError("Username 4+ belgi bo'lishi kerak")
            elif len(username)>20:
                raise forms.ValidationError("Username 20dan kam belgi bo'lishi kerak")

        return self.cleaned_data
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"form-control"}))

    def clean(self):
        password = self.cleaned_data.get('password',None)
        confirm_password = self.cleaned_data.get('confirm_password',None)
        if  password:
            if confirm_password !=password:
                raise forms.ValidationError('Password xato takrorlandi')
            elif len(password)<7:
                raise forms.ValidationError("password 8 ta belgidan kam bo'lmasligi kerak")
                
        return self.cleaned_data
    
class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    phone_number = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    def check_phone(self):
        phone_number = self.cleaned_data.get('phone_number',None)
        if phone_number:
            if phone_number[:4]!='+998':
                raise forms.ValidationError('Raqam uzbga tegishli ekanligini tekshiring')
            elif phone_number[:4]!='+998'and len(phone_number)!=13:
                raise forms.ValidationError('raqam 12 ta ekanligini tekshiring ') 
        return self.cleaned_data

    bio = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(required=False,widget=forms.EmailInput(attrs={"class":"form-control"}))
    photo = forms.ImageField(required=False,widget=forms.FileInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields= ('username','first_name','last_name','bio','phone_number','photo','email')

  