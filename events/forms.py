from django import forms
from .models import Event, Application, Response


class EventCreationForm(forms.ModelForm):
    """Форма для создания спортивного мероприятия (события)"""
    class Meta:
        model = Event
        fields = ('title', 'event_type', 'location', 'description', 'event_date')
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'})
        }


class MarathonJoinForm(forms.ModelForm):
    """Форма для заявки на марафон (1 тип событий)"""
    class Meta:
        model = Application
        fields = ['description']


class CompetitionJoinForm(forms.ModelForm):
    """Форма для отклика на соревнование (2 тип событий)"""
    class Meta:
        model = Response
        fields = ['title', 'description', 'command', 'rank', 'document']
