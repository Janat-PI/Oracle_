from django import forms

from .models import Student
from .helpers import send_message_for_student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class SendForm(forms.Form):

    some_text = forms.CharField(max_length=255, label="some_text")


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.email = kwargs.pop("email")
        super().__init__(*args, **kwargs)


    def save(self):
        some_text = self.cleaned_data["some_text"]
        send_message_for_student(
            self.request.user.email,
            some_text,
            self.email
        )