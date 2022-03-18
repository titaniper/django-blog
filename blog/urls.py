from django.urls import path, include
# from blog import views

# NOTE: .로 찍어주는 것이 리팩토링 할때 편하다.
from . import views

urlpatterns = [
    path('', views.index),
]
