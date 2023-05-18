from django.urls import path
from .views import ListType,List_Type_and_Event
urlpatterns = [
    path("list_type/",ListType.as_view(),name="list_type"),
    path("type_event/",List_Type_and_Event.as_view(),name="list_type_event"),

]