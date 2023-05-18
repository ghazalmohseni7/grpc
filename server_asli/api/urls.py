from django.urls import path
from api.views import ListEvents
urlpatterns = [
    path("list_event/",ListEvents.as_view(),name="list_event"),

]