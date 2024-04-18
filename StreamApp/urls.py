from django.urls import path

from . import views

urlpatterns = [path('Stream', views.Stream, name="Stream"),
]