from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.exceptions import ObjectDoesNotExist
from .models import User

class UserRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Masukkan Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Emailmu bro'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password sing aman yo!'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Baleni passwordmu sing nong nduwur'})

    class Meta:
        model = User
        fields = ("username",
                  "email",
                  "gender",
                  "password1",
                  "password2")

    def clean_username(self):
        username = self.cleaned_data['username']
        print(username)
        if ' ' in username:
            raise forms.ValidationError("Username ra usah gawe spasi to")
        return username

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class UserLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields['email'].widget.attrs.update({'placeholder': 'Masukkan Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Ini Password bro'})

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if email and password:
            self.user = authenticate(email=email, password=password)
            if self.user is None:
                if User.objects.filter(email=email).exists():
                    raise forms.ValidationError("Salah passwordmu")
                else:
                    raise forms.ValidationError("Usermu belum terdaftar")
            if not self.user.is_active:
                raise forms.ValidationError("Kowe belum aktif")
        return super().clean(*args, **kwargs)

    def get_user(self):
        return self.user