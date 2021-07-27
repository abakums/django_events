from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Event, Application, Response
from .forms import EventCreationForm, MarathonJoinForm, CompetitionJoinForm
from django.conf import settings
from django.core.mail import send_mail
from.decorators import group_required


def home_page(request):
    """Рендеринг главной страницы сайта"""
    return render(request, 'index.html')


@login_required
def events_page(request):
    """Рендеринг страницы со всеми спортивными мероприятиями"""
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})


@group_required('Organizer')
def event_creation(request):
    """Рендеринг страницы создания нового события и перенаправление на страницу всех событий после отправки формы"""
    if request.method == 'POST':
        event_form = EventCreationForm(request.POST)
        if event_form.is_valid():
            new_event = event_form.save(commit=False)
            new_event.organizer = request.user
            new_event.save()
            return redirect('/events/')
    else:
        event_form = EventCreationForm()
    return render(request, 'event_creation.html', {'event_form': event_form})


@group_required('Participant')
def marathon_join(request, pk):
    """Рендеринг страницы создания новой заявки и перенаправление на страницу всех событий после отправки формы"""
    if request.method == 'POST':
        marathon_form = MarathonJoinForm(request.POST)
        if marathon_form.is_valid():
            new_application = marathon_form.save(commit=False)
            new_application.participant = request.user
            event = Event.objects.get(pk=pk)
            new_application.event = event
            new_application.save()
            title = 'Новый участник марафона!'
            text = settings.MESSAGE.format(event, request.user, request.user.email)
            org = User.objects.get(pk=event.organizer.pk)
            send_mail(title, text, settings.EMAIL_HOST_USER, [org.email], fail_silently=False)
            return redirect('/events/')
    else:
        marathon_form = MarathonJoinForm()
    return render(request, 'marathon_join_form.html', {'marathon_form': marathon_form, 'pk': pk})


@group_required('Participant')
def competition_join(request, pk):
    """Рендеринг страницы создания нового отклика и перенаправление на страницу всех событий после отправки формы"""
    if request.method == 'POST':
        competition_form = CompetitionJoinForm(request.POST, request.FILES)
        if competition_form.is_valid():
            new_response = competition_form.save(commit=False)
            new_response.participant = request.user
            event = Event.objects.get(pk=pk)
            new_response.event = event
            new_response.save()
            title = 'Новый участник соревнований!'
            text = settings.MESSAGE.format(event, request.user, request.user.email)
            org = User.objects.get(pk=event.organizer.pk)
            send_mail(title, text, settings.EMAIL_HOST_USER, [org.email], fail_silently=False)
            return redirect('/events/')
    else:
        competition_form = CompetitionJoinForm()
    return render(request, 'competition_join_form.html', {'competition_form': competition_form, 'pk': pk})


@group_required('Organizer')
def user_events(request, pk):
    """Рендериинг страницы со всеми событиями текущего авторизованного пользователя (Организатора)"""
    events = Event.objects.filter(organizer=pk)
    return render(request, 'user_events.html', {'user_events': events})


@group_required('Organizer')
def user_event(request, user_pk, event_pk):
    """Рендериинг страницы с определенным событием текущего авторизованного пользователя (Организатора)"""
    if request.user.pk == user_pk:
        event = Event.objects.get(pk=event_pk)
        if event.event_type == 1:
            replies = Application.objects.filter(event=event)
        else:
            replies = Response.objects.filter(event=event)
        return render(request, 'user_event.html', {'event': event, 'replies': replies, 'MEDIA_URL': settings.MEDIA_URL})
    else:
        return redirect('')


@group_required('Participant')
def user_applications(request, pk):
    """Рендеринг страницы со всеми заявками на мероприятия(события 1 типа) текущего пользователя (Участника)"""
    applications = Application.objects.filter(participant=User.objects.get(pk=pk))
    return render(request, 'user_applications.html', {'applications': applications})


@group_required('Participant')
def user_responses(request, pk):
    """Рендеринг страницы со всеми откликами на мероприятия(события 2 типа) текущего пользователя (Участника)"""
    responses = Response.objects.filter(participant=User.objects.get(pk=pk))
    return render(request, 'user_responses.html', {'responses': responses,  'MEDIA_URL': settings.MEDIA_URL})
