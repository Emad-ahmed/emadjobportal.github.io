from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from jobapp.models.userinfo import UserInfo
from django.core import validators

CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]


class SignForm(ModelForm):

    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model = UserInfo
        fields = ['name', 'email', 'gender',
                  'address', 'password', 're_password', 'images']
        labels = {'re_password': 'Password Confirmation'}

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'address': forms.Textarea(attrs={'class': 'form-control'}),
                   'password': forms.PasswordInput(attrs={'class': 'form-control'}),
                   're_password': forms.PasswordInput(attrs={'class': 'form-control'}), }

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if not password:
            raise forms.ValidationError("Password Enter Must")

        if password != re_password:
            raise forms.ValidationError("Password Not Match")

        return re_password

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if (UserInfo.objects.filter(email=email).exists()):
            raise forms.ValidationError("Email Already Exists")

        return email

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if(len(name) < 3):
            raise forms.ValidationError("Name Must Be More Than 3 Character")
        return name
