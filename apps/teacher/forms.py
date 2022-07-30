from django.contrib.auth import get_user_model, authenticate
from django import forms
from django.contrib.auth.forms import AuthenticationForm


from .models import UserTeacher



class CustomAuthenticationForm(AuthenticationForm):

    number_phone = forms.CharField()

    def clean(self):
        number_phone = self.cleaned_data.get("number_phone")
        password = self.cleaned_data.get("password")

        if number_phone is not None and password:
            self.user_cache = authenticate(
                self.request, number_phone=number_phone, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data



class TeacherForm(forms.ModelForm):
    
    class Meta:
        model = UserTeacher
        fields = "__all__"


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(max_length=8,
                               widget=forms.PasswordInput,
                               required=True)
    password_confirm = forms.CharField(max_length=8,
                                       widget=forms.PasswordInput,
                                       required=True)

    username = forms.CharField(max_length=255, required=True)
    
    class Meta:
        model = UserTeacher
        fields = ["number_phone", 'username', 'password', 'password_confirm',
                  'first_name', 'last_name']

    def clean_number_phone(self):
        number_phone = self.cleaned_data.get('number_phone')
        if UserTeacher.objects.filter(number_phone=number_phone).exists():
            raise forms.ValidationError('Пользователь уже зарегистрирован')
        return number_phone

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if not username:
    #         raise forms.ValidationError('username уже зарегистрирован')

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.pop('password_confirm')
        if password_confirm != password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    def save(self):
        user = UserTeacher.objects.create(**self.cleaned_data)
        # user.create_activation_code()
        # send_activation_mail(user.email, user.activation_code)
        return user