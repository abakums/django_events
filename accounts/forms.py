from django.contrib.auth.models import User
from django import forms

# варианты выбора ролей пользователей
GROUPS_CHOICES = [
    ('Organizer', 'Организатор'),
    ('Participant', 'Участник'),
]


class RegisterForm(forms.ModelForm):
    """Форма регистрации на сайте"""
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    group = forms.ChoiceField(label='Регистрация в качестве', choices=GROUPS_CHOICES, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'email'
        }
        help_texts = {
            'username': None
        }


class LoginForm(forms.ModelForm):
    """Форма авторизации на сайте"""
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {'username': 'Логин',
                  'password': 'Пароль'}
        help_texts = {
            'username': None
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'type': 'password'})
        }
