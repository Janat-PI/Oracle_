from django.contrib.auth import get_user_model
from django import forms


User = get_user_model()



class RegistrationForm(forms.ModelForm):

    password = forms.CharField(max_length=8,
                               widget=forms.PasswordInput,
                               required=True)
    password_confirm = forms.CharField(max_length=8,
                                       widget=forms.PasswordInput,
                                       required=True)

    class Meta:
        model = User
        fields = ['username',  'password', 'password_confirm']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь уже зарегистрирован')
        return username

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.pop('password_confirm')
        if password_confirm != password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    def save(self):
        user = User.objects.create(**self.cleaned_data)
        return user