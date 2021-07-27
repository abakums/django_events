from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    """Функция авторизации пользователя на сайте"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/events/')
            else:
                return HttpResponse('Неактивный аккаунт')
        else:
            return HttpResponse('Неверные данные для входа')
    else:
        user_form = LoginForm()
    return render(request, 'login.html', {'user_form': user_form})


def add_permissions(group):
    """Функционал добавления прав для каждой группы пользователей при их создании"""
    if group.name == 'Organizer':
            group.permissions.add(Permission.objects.get(codename='add_event'))
    else:
            group.permissions.add(Permission.objects.get(codename='add_application'))
            group.permissions.add(Permission.objects.get(codename='add_response'))


def user_register(request):
    """Функция регистрации пользователя"""
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.data['password'] != user_form.data['password2']:
            user_form.add_error('password', 'Введенные пароли не совпадают!')
        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            group, created = Group.objects.get_or_create(name=user_form.cleaned_data['group'])
            new_user.groups.add(group)
            if created:
                add_permissions(group)
            login(request, new_user)
            return redirect('/events/')
    else:
        user_form = RegisterForm()
    return render(request, 'register.html', {'user_form': user_form})


@login_required
def user_logout(request):
    """Функция для выхода из системы пользователя(для его разлогинизации)"""
    logout(request)
    return redirect('/')
