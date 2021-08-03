from django.urls import path, include
from .views import LocaionsViewSet



urlpatterns = [
    path('', LocaionsViewSet.as_view()),
]
