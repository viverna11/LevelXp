from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Електронна пошта')            

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': "Ім'я користувача",
        }

    # Ця штука переводить текст форми і забирає підказки так шо не трогайте
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "Пароль"
        self.fields['password2'].label = "Підтвердження пароля"

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None