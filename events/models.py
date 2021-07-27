from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    """Спортивные мероприятия"""
    # варианты выбора спортивного мероприятия
    EVENT_TYPES = [
        (1, 'Марафон'),  # на марафон оставляется заявка на участие
        (2, 'Соревнование')  # на соревнование оставляется отклик с файлом, содержащим необходимые документы для допуска
    ]

    title = models.CharField(verbose_name='Название события', max_length=200)
    event_type = models.PositiveSmallIntegerField(verbose_name='Тип события', choices=EVENT_TYPES)
    location = models.CharField(verbose_name='Место проведения', max_length=200)
    description = models.TextField(verbose_name='Описание события')
    published_date = models.DateField(verbose_name='Дата размещения', auto_now_add=True)
    event_date = models.DateField(verbose_name='Дата события')
    organizer = models.ForeignKey(User, verbose_name='Организатор', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class Application(models.Model):
    """Заявки на марафоны"""
    description = models.TextField(verbose_name='Примечание')
    participant = models.ForeignKey(User, verbose_name='Участник', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, verbose_name='Событие', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.participant) + ' ' + str(self.event)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Response(models.Model):
    """Отклики на соревнования"""
    participant = models.ForeignKey(User, verbose_name='Участник', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, verbose_name='Событие', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    description = models.TextField(verbose_name='Примечание')
    command = models.CharField(verbose_name='Спортивный клуб', max_length=200)
    rank = models.CharField(verbose_name='Спортивный разряд', max_length=50)
    document = models.FileField(verbose_name='Документы', upload_to='documents/')

    def __str__(self):
        return str(self.participant) + ' ' + str(self.event)

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
