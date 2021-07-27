from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('events/', events_page, name='events_page'),
    path('event_creation/', event_creation, name='event_creation'),
    path('marathon_join/<int:pk>', marathon_join, name='marathon_join'),
    path('competition_join/<int:pk>', competition_join, name='competition_join'),
    path('user_events/<int:pk>', user_events, name='user_events'),
    path('user_event/<int:user_pk>/<int:event_pk>', user_event, name='user_event'),
    path('user_applications/<int:pk>', user_applications, name='user_applications'),
    path('user_responses/<int:pk>', user_responses, name='user_responses')
]
